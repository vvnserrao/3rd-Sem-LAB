import numpy as np


X = np.array([1, 2, 3, 4, 5, 6, 7])
Y = np.array([1.5, 3.8, 6.7, 9.0, 11.2, 13.6, 16])


X_b = np.c_[np.ones((X.shape[0], 1)), X]  


X_b_T = X_b.T
theta = np.linalg.inv(X_b_T.dot(X_b)).dot(X_b_T).dot(Y)


def compute_cost(X, Y, theta):
    m = len(Y)
    predictions = X.dot(theta)
    error = predictions - Y
    cost = (1 / (2 * m)) * np.sum(np.square(error))
    return cost


final_cost = compute_cost(X_b, Y, theta)

print(f"Parameters (theta): {theta}")
print(f"Final cost: {final_cost}")


def predict(X, theta):
    X_b = np.c_[np.ones((X.shape[0], 1)), X]  
    return X_b.dot(theta)


predictions = predict(X, theta)
print(f"Predictions: {predictions}")


import matplotlib.pyplot as plt

plt.scatter(X, Y, color='blue', label='Data Points')
plt.plot(X, predictions, color='red', label='Fitted Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Linear Regression using Matrix Multiplication')
plt.legend()
plt.show()
