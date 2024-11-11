import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"Sample_Datasets\linear_reg_dataset.csv")  
x = data['Square_Footage']  
y = data['Price']  
x = np.array(x)
y = np.array(y)
n = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
numerator = np.sum((x - x_mean) * (y - y_mean))
denominator = np.sum((x - x_mean) ** 2)
m = numerator / denominator
b = y_mean - (m * x_mean)
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")
y_pred = m * x + b
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, y_pred, color='red', label='Regression Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression Fit')
plt.legend()
plt.show()