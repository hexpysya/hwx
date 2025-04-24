# Linear Regression Implementation Project

This project demonstrates different approaches to implementing linear regression:
1. Custom analytical solution using the least squares method
2. NumPy's polyfit function
3. Gradient descent optimization algorithm

## Overview

This project implements and compares three different methods for linear regression on simulated data. The implementation generates noisy linear data and then fits regression lines using:
- A custom analytical implementation of the least squares method
- NumPy's built-in polyfit function
- A custom gradient descent implementation

The project visualizes the results, showing how each method performs compared to the original parameters.

## Implementation Details

### Data Generation

The script generates synthetic data with a known linear relationship (y = kx + b) and adds Gaussian noise. This allows us to compare how well each method recovers the original parameters.

### Methods Implemented

1. **Analytical Least Squares Solution**
   - The `sqa()` function implements the analytical solution for linear regression
   - Uses the formula: k = Σ[(x-x̄)(y-ȳ)] / Σ[(x-x̄)²]

2. **NumPy Implementation**
   - Uses NumPy's `polyfit()` function to find the best fit

3. **Gradient Descent**
   - The `gradient()` function implements gradient descent optimization
   - Updates parameters iteratively by moving against the gradient of the MSE
   - Learning rate and number of iterations can be adjusted

### Visualizations

The project provides visualizations to compare:
- Original data with fitted lines from each method
- The error (MSE) over iterations for the gradient descent method

## Results

The visual comparison shows how each method performs in finding the underlying linear relationship in the noisy data. The analytical and NumPy methods typically produce identical results, while the gradient descent approach converges to a similar solution after sufficient iterations.


### Least Squares Method

The solution minimizes the sum of squared residuals between the observed and predicted values:

- k (slope) = Σ[(x-x̄)(y-ȳ)] / Σ[(x-x̄)²]
- b (intercept) = ȳ - k·x̄

### Gradient Descent

Gradient descent updates parameters in the direction that minimizes the error:

- MSE = (1/n) · Σ(y - (kx + b))²
- Partial derivatives:
  - ∂MSE/∂k = (-2/n) · Σ[x·(y-(kx+b))]
  - ∂MSE/∂b = (-2/n) · Σ[y-(kx+b)]
