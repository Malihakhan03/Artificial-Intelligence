# Step 1: Import Libraries
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Data Collection (Real Dataset)
X = np.array([50, 100, 150, 200, 250, 300, 350, 400])   # Distance (km)
Y = np.array([5, 8, 12, 15, 18, 22, 25, 28])            # Fuel used (liters)

# Step 3: Calculation (Finding slope m and intercept c)
n = len(X)

sum_x = np.sum(X)
sum_y = np.sum(Y)
sum_xy = np.sum(X * Y)
sum_x2 = np.sum(X * X)

# Calculate slope (m)
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x ** 2))

# Calculate intercept (c)
c = (sum_y - m * sum_x) / n

print("Slope (m):", m)
print("Intercept (c):", c)

# Step 4: Prediction using user input
x_new = float(input("Enter distance (in km) to predict fuel usage: "))
y_pred_new = m * x_new + c

print("Predicted Fuel used for", x_new, "km:", y_pred_new)

# Step 5: Visualization
Y_pred = m * X + c

plt.scatter(X, Y)        # Actual data points
plt.plot(X, Y_pred)      # Regression line
plt.xlabel("Distance (km)")
plt.ylabel("Fuel Used (liters)")
plt.title("Linear Regression - Distance vs Fuel Consumption")
plt.show()