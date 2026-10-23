import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_avrami(file_path, sheet_name):
    """
    Reads isothermal DSC data from an Excel sheet and calculates 
    the Avrami macrokinetic parameters (n_a and K_av).
    """
    print(f"--- Analyzing {sheet_name} ---")
    
    # 1. Read the Excel sheet
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # 2. Identify the time column (handling slight naming variations like 'time (s)' or 'Time (s)')
    time_col = [c for c in df.columns if 'ime' in c][0]
    
    # 3. Filter data for the Primary Crystallization phase: 0.1 <= X(t) <= 0.8
    # This matches the boundaries defined in TA Instruments Note 425
    mask = (df['X(t)'] >= 0.1) & (df['X(t)'] <= 0.8)
    df_filtered = df[mask].copy()
    
    # 4. Apply Avrami Linearization transformations
    # x = log(t)
    # y = log(-ln(1 - X(t)))
    df_filtered['log_t'] = np.log10(df_filtered[time_col])
    df_filtered['log_ln'] = np.log10(-np.log(1 - df_filtered['X(t)']))
    
    # 5. Perform Linear Regression (Least Squares Method)
    # np.polyfit returns [slope, intercept]
    coefficients = np.polyfit(df_filtered['log_t'], df_filtered['log_ln'], 1)
    
    n_a = coefficients[0]        # Slope = Avrami Exponent
    log_k = coefficients[1]      # Intercept = log(K_av)
    k_av = 10 ** log_k           # Rate Constant
    
    print(f"Calculated Parameters:")
    print(f"Avrami Exponent (n_a) = {n_a:.4f}")
    print(f"Rate Constant (K_av)  = {k_av:.2e}")
    print(f"Intercept (log K_av)  = {log_k:.4f}\n")
    
    return df_filtered, n_a, log_k

if __name__ == "__main__":
    # Define the file name and the specific sheets to analyze
    excel_file = 'ASSIGNMENT 3.xlsx'
    temperatures = ['DSC 270', 'DSC 280', 'DSC 285', 'DSC 290']
    
    # Loop through each temperature sheet and run the analysis
    for temp in temperatures:
        try:
            analyze_avrami(excel_file, temp)
        except Exception as e:
            print(f"Error processing {temp}: Ensure the file is in the same directory.")