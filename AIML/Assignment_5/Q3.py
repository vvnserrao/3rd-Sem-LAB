# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset from a CSV file (update the file path accordingly)
data = pd.read_csv('hprice.csv')

# Define independent (X) and dependent (y) variables
X = data['total_sqft_int'].values.reshape(-1, 1)  # Independent variable: total square footage
y = data['price'].values  # Dependent variable: house price

# Add a bias term (intercept) to the feature matrix
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Adding a column of ones for the intercept

# Calculate the coefficients using the Normal Equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Extract the slope (m) and intercept (c) from theta
c = theta_best[0]
m = theta_best[1]

# Make predictions on the dataset using the calculated coefficients
y_pred = X_b.dot(theta_best)

# Calculate Root Mean Square Error (RMSE) and R-squared (R²)
rmse = np.sqrt(np.mean((y - y_pred) ** 2))
r2 = 1 - (np.sum((y - y_pred) ** 2) / np.sum((y - np.mean(y)) ** 2))

# Print the RMSE and R² to evaluate the model's performance
print(f"Root Mean Square Error (RMSE): {rmse}")
print(f"R-squared value: {r2}")

# Create an array of new total_sqft_int values
new_total_sqft_int = np.array([1200, 1500, 1800, 2000])

# Add a bias term for the new input values
new_X_b = np.c_[np.ones((new_total_sqft_int.shape[0], 1)), new_total_sqft_int]

# Predict the prices for the new values using matrix multiplication
new_prices = new_X_b.dot(theta_best)

# Print the predicted prices
for i, sqft in enumerate(new_total_sqft_int):
    print(f"Predicted price for {sqft} sq. ft.: ${new_prices[i]:.2f}")
