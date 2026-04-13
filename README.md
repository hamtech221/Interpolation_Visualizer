# 📈 Interpolation Visualizer (Python GUI)

## 📌 Overview

This project implements an **interactive data interpolation tool** using Python and Tkinter.

It allows users to load CSV data, apply different interpolation techniques, and visualize results dynamically using Matplotlib. The application is designed to help understand how interpolation methods behave on real datasets.

---

## ⚙️ System Architecture

**CSV Data → Interpolation Method Selection → Curve Generation → Visualization → Export Plot**

---

## 🔧 Key Features

* Load and parse CSV datasets (x, y values)
* Multiple interpolation methods:

  * Linear
  * Cubic Spline
  * Nearest Neighbor
* Real-time plotting of original and interpolated data
* Built-in explanation of method selection
* Save plots as PNG images

---

## 🧠 Engineering Concepts

* Numerical Interpolation
* Curve Fitting
* Piecewise Linear Interpolation
* Cubic Spline Interpolation
* Data Visualization

---

## 📊 Results

The application visualizes:

* Original data points
* Interpolated curve based on selected method

### 📷 Sample Outputs

> Add your screenshots inside an `images/` folder and update paths below

![Interpolation Plot](images/interpolation_plot.png)

---

## 🛠️ Tools & Technologies

* Python
* Tkinter (GUI)
* NumPy
* SciPy
* Matplotlib

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```bash
   pip install numpy matplotlib scipy
   ```
3. Run the script:

   ```bash
   python main.py
   ```
4. Load a CSV file with at least two columns (x, y) or choose the file given here. You can modify the values according to your needs.
5. Select an interpolation method and click **Plot**
