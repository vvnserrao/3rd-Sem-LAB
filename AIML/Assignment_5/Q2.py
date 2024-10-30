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
# theta = (X_b^T * X_b)^(-1) * X_b^T * y
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

# Visualize the regression line and scatter plot
plt.scatter(X, y, color='blue', label='Actual Data')  # Scatter plot of actual data points
plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line')  # Regression line
plt.xlabel('Total Square Feet (int)')
plt.ylabel('Price')
plt.title('Linear Regression - Price vs. Total Square Feet')
plt.legend()
plt.show()  # Display the plot
