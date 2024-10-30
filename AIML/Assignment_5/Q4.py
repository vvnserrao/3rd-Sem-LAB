# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Load the dataset from a CSV file (update the file path accordingly)
data = pd.read_csv('hprice.csv')

# Define independent (X) and dependent (y) variables
X = data['total_sqft_int'].values.reshape(-1, 1)  # Independent variable: total square footage
y = data['price'].values  # Dependent variable: house price

# Split the data into training (75%) and testing (25%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Add a bias term (intercept) to the feature matrix
X_b_train = np.c_[np.ones((X_train.shape[0], 1)), X_train]  # Adding a column of ones for the intercept
X_b_test = np.c_[np.ones((X_test.shape[0], 1)), X_test]  # Adding a column of ones for the intercept

# Calculate the coefficients using the Normal Equation
theta_best = np.linalg.inv(X_b_train.T.dot(X_b_train)).dot(X_b_train.T).dot(y_train)

# Predict prices for the test set using matrix multiplication
y_pred_test = X_b_test.dot(theta_best)

# Create an array of new total_sqft_int values to predict prices for
new_total_sqft_int = np.array([1200, 1500, 1800, 2000]).reshape(-1, 1)

# Add a bias term for the new input values
new_X_b = np.c_[np.ones((new_total_sqft_int.shape[0], 1)), new_total_sqft_int]

# Predict the prices for the new values using matrix multiplication
new_prices = new_X_b.dot(theta_best)

# Plot the graph
plt.scatter(X_test, y_test, color='blue', label='Actual Data')  # Scatter plot of actual data points
plt.plot(X_test, y_pred_test, color='red', linewidth=2, label='Regression Line')  # Regression line for test data
plt.scatter(new_total_sqft_int, new_prices, color='green', marker='o', label='Predicted Prices')  # Predicted prices for new values
plt.xlabel('Total Square Feet (int)')
plt.ylabel('Price')
plt.title('Linear Regression - Price vs. Total Square Feet')
plt.legend()
plt.show()  # Display the plot

# Print the predicted prices for new values
for i, sqft in enumerate(new_total_sqft_int):
    print(f"Predicted price for {sqft[0]} sq. ft.: ${new_prices[i]:.2f}")
