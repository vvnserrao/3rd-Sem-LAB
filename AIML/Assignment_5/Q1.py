# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file (assuming you have a 'headbrain.csv' file)
data = pd.read_csv('headbrain.csv')

# Display the shape (number of rows and columns) of the dataset
print(data.shape)

# Display the first few rows of the dataset to get an overview
print(data.head())

# Extract the 'Head Size(cm^3)' and 'Brain Weight(grams)' columns as X and Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

# Reshape X to be a 2D array and add a bias term (intercept)
X = X.reshape(-1, 1)
X_b = np.c_[np.ones((X.shape[0], 1)), X]  # Add bias term (intercept)

# Step to compute the parameters using the Normal Equation
# theta = (X_b^T * X_b)^(-1) * X_b^T * Y
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y)

# Extract the slope (m) and intercept (c) from theta
c = theta_best[0]
m = theta_best[1]

# Print the coefficients
print("Slope (m):", m)
print("Intercept (c):", c)

# Define a function to predict brain weight based on the linear regression model
def predict(c, m, X):
    return c + (m * X)

# Get a new head size value from the user
new_head_size = int(input("Enter a new value:"))

# Use the predict function to calculate the predicted brain weight
predicted_brain_weight = predict(c, m, new_head_size)

# Print the predicted brain weight for the new head size
print("Predicted Brain Weight for", new_head_size, ":", predicted_brain_weight)

# Calculate the range of x values for the regression line
max_x = np.max(X) + 100
min_x = np.min(X) - 100

# Generate a range of x values for the regression line
x = np.linspace(min_x, max_x, 1000)

# Calculate the corresponding y values using the linear regression model
y = predict(c, m, x)

# Plot the regression line and scatter plot of the data points
plt.plot(x, y, color='black', label='Regression Line')
plt.scatter(X, Y, c='red', label='Scatter Plot')

# Add labels and a legend to the plot
plt.xlabel('Head Size in cm³')
plt.ylabel('Brain Weight in grams')
plt.legend()

# Display the plot
plt.show()
