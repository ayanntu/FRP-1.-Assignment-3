[readme.md](https://github.com/user-attachments/files/33893258/readme.md)
# PEEK Isothermal Crystallization Kinetics Analysis

**Course:** European Master in Advanced Structural Analysis and Design using Composite Materials (FRP++)  
**Module:** FRP++ 1 - Virtual Manufacturing (Assignment 3)  
**Topic:** Simulating the crystallization of thermoplastic matrix composites

## 📌 Project Overview
This repository contains the Excel workbook used to analyze the isothermal crystallization kinetics of a Polyetheretherketone (PEEK) thermoplastic matrix. The analysis is based on raw experimental Differential Scanning Calorimetry (DSC) data. 

The primary objective of this project is to process the raw thermal data, calculate the relative degree of crystallinity over time $X(t)$, and extract the macroscopic kinetic parameters using the **Avrami macrokinetic model**. These parameters are essential inputs for virtual manufacturing simulations, enabling the prediction of optimal cooling cycles during thermoplastic composite manufacturing (e.g., hot pressing, automated tape placement).

## 📁 File Contents
The provided Excel workbook (`ASSIGNMENT 3.xlsx`) contains distinct worksheets for four different isothermal holding temperatures: **270 °C, 280 °C, 285 °C, and 290 °C**. 

Each sheet contains:
1. **Raw DSC Data:** Time (s) and exothermic Heat Flow (mW/g).
2. **Numerical Integration:** Calculation of cumulative enthalpy (J/g) using the trapezoidal rule.
3. **Relative Crystallinity $X(t)$:** Calculated by dividing the cumulative enthalpy by the maximum theoretical enthalpy of 100% crystalline PEEK (approx. 130 J/g).
4. **Avrami Linearization:** Mathematical transformation to extract kinetic parameters.
5. **Graphical Plots:** 
   - Heat flow vs. time
   - Cumulative enthalpy vs. time
   - Relative crystallinity $X(t)$ vs. time
   - Linearized Avrami plots $\log(-\ln(1-X(t)))$ vs. $\log(t)$

## 🧮 Methodology

### 1. Relative Crystallinity
The evolution of crystallinity is determined by integrating the DSC heat flow signal:
$$X(t) = \frac{\int_0^t (dH_c/dt) dt}{\Delta H_c}$$

### 2. The Avrami Model
The primary crystallization phase is modeled using the Avrami equation:
$$X(t) = 1 - \exp(-K_{av} t^{n_a})$$

To extract the Avrami geometric exponent ($n_a$) and the crystallization rate constant ($K_{av}$), the equation is linearized:
$$\log(-\ln(1 - X(t))) = \log(K_{av}) + n_a \log(t)$$

*Note: The linear regression is strictly applied within the boundaries of **$X(t) \in [0.1, 0.8]$**. This limits the analysis to the primary crystallization phase (free spherulitic growth) and excludes secondary crystallization (impingement), which deviates from the Avrami assumptions.*

## 📊 Summary of Results
The extracted kinetic parameters successfully demonstrate the profound effect of undercooling on the crystallization rate of PEEK. As the temperature approaches the melting point, the crystallization rate drops by two orders of magnitude, and the crystal growth geometry shifts from mixed 1D/2D to predominantly 2D planar structures.

| Isothermal Temperature (°C) | Avrami Exponent ($n_a$) | Rate Constant ($K_{av}$) |
| :---: | :---: | :---: |
| **270** | 1.695 | 1.73 × 10⁻⁴ |
| **280** | 1.376 | 3.86 × 10⁻⁴ |
| **285** | 2.179 | 3.40 × 10⁻⁶ |
| **290** | 2.071 | 1.89 × 10⁻⁶ |

## 🛠 Usage
Download the `.xlsx` file and open it in Microsoft Excel. Each tab is fully formulated. You can inspect the cells in the Avrami linearization columns to see the exact implementation of the boundary limits and least-squares interpolation used to derive the constants.

## 📖 References
* Supaphol, P., & Spruiell, J.E. (2001). *Isothermal melt and cold crystallization kinetics and subsequent melting behavior in syndiotactic polypropylene*. Polymer, 42, 699-712.
* TA Instruments (Application Note TA425). *Applying the Avrami and Malkin Macrokinetic Models for Evaluating Isothermal Crystallization Kinetics*.
