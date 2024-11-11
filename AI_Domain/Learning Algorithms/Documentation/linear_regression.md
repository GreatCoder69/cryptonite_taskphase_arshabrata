# Linear Regression
## Model Representation
### Notation Guide
![s15445111112024](https://a.okmd.dev/md/6731d924d9a9a.png)
### Problem Statement
The goal is to fit a linear regression model to a dataset containing two data points on housing prices and sizes. These data points represent houses of 1000 sqft and 2000 sqft, with prices of $300,000 and \$500,000, respectively. The task involves building a model that uses this data to predict house prices for different sizes, such as a house with 1200 sqft.
![s15460411112024](https://a.okmd.dev/md/6731d96648e29.png)
### Working Method 
To set up the model, we create the feature and target variables using NumPy arrays:
```
x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
```
The variable m represents the number of training examples and can be derived using x_train.shape[0]. Alternatively, m can be computed using Python's len() function.
```
m = x_train.shape[0]
```
Using Matplotlib's scatter() function, we can plot the training data points.
```
plt.scatter(x_train, y_train, marker='x', c='r')
plt.title("Housing Prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000 sqft)')
plt.show()
```
The linear regression model is represented as follows where where different values of w(weight) and b(bias) give different straight lines in the plot.:
![s15522111112024](https://a.okmd.dev/md/6731dae091ab0.png)
To compute output for each data point, we use the function :
```
def compute_model_output(x, w, b):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
    return f_wb
```
Using this function, we can plot our model prediction against actual values:
```
tmp_f_wb = compute_model_output(x_train, w, b)
plt.plot(x_train, tmp_f_wb, c='b', label='Our Prediction')
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')
plt.title("Housing Prices")
plt.ylabel('Price (in 1000s of dollars)')
plt.xlabel('Size (1000 sqft)')
plt.legend()
plt.show()
```
To make a prediction for a house with 1200 sqft, use x_i = 1.2 since the units are in 1000 sqft:
```
w = 200                         
b = 100    
x_i = 1.2
cost_1200sqft = w * x_i + b    
print(f"${cost_1200sqft:.0f} thousand dollars")
```
## Cost Function
The following libraries are used :
```
import numpy as np
%matplotlib widget
import matplotlib.pyplot as plt
from lab_utils_uni import plt_intuition, plt_stationary, plt_update_onclick, soup_bowl
plt.style.use('./deeplearning.mplstyle')
```
### Problem Statement
You would like a model which can predict housing prices given the size of the house.
Let's use the same two data points as before the previous lab- a house with 1000 square feet sold for $300,000 and a house with 2000 square feet sold for \$500,000.
![s15581011112024](https://a.okmd.dev/md/6731dc3c29037.png)
### Computing Cost
The term cost here refers to how well the model's predictions align with the actual prices. The cost function provides a measure of prediction accuracy by comparing the predicted and actual values.
![s16010411112024](https://a.okmd.dev/md/6731dceb7cd62.png)
The goal is to find values of w and b to minimize J(w,b).  
The code below calculates the cost function by iterating through each training example, calculating the squared error, and summing these values.
```
def compute_cost(x, y, w, b): 
    m = x.shape[0] 
    cost_sum = 0 
    
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum += cost
    
    total_cost = (1 / (2 * m)) * cost_sum  
    return total_cost
```
The goal is to find f(x)=wx+b that accurately predicts house prices. The cost function J(w,b) indicates prediction accuracy, i.e., if w and b are optimized, f(x) will closely match  y, and the cost will be minimized.
## Gradient Descent
### Working
Our cost function, implemented previously, is essential for calculating the error of our model.
```
def compute_cost(x, y, w, b):
    m = x.shape[0]
    cost = 0
    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i]) ** 2
    total_cost = 1 / (2 * m) * cost
    return total_cost
```
![s16112511112024](https://a.okmd.dev/md/6731df5776bba.png)
The gradient function below calculates the partial derivatives with respect to w and b:
```
def compute_gradient(x, y, w, b): 
    m = x.shape[0]
    dj_dw, dj_db = 0, 0
    
    for i in range(m):  
        f_wb = w * x[i] + b 
        dj_dw += (f_wb - y[i]) * x[i]
        dj_db += f_wb - y[i]
    dj_dw /= m 
    dj_db /= m 
    return dj_dw, dj_db
```
The plot shows the direction and magnitude of gradients at different points, guiding our parameter updates : 
```
plt_gradients(x_train, y_train, compute_cost, compute_gradient)
plt.show()
```
The following function implements gradient descent. Each iteration updates w and b using the computed gradients.
```
def gradient_descent(x, y, w_in, b_in, alpha, num_iters, cost_function, gradient_function): 
    J_history, p_history = [], []
    b, w = b_in, w_in
    
    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w, b)
        b -= alpha * dj_db
        w -= alpha * dj_dw
        if i < 100000:
            J_history.append(cost_function(x, y, w, b))
            p_history.append([w, b])
        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4}: Cost {J_history[-1]:0.2e} ",
                  f"dj_dw: {dj_dw: 0.3e}, dj_db: {dj_db: 0.3e}  ",
                  f"w: {w: 0.3e}, b:{b: 0.5e}")
    return w, b, J_history, p_history
```
Running gradient descent: 
```
w_init, b_init = 0, 0
iterations, tmp_alpha = 10000, 1.0e-2
w_final, b_final, J_hist, p_hist = gradient_descent(
    x_train, y_train, w_init, b_init, tmp_alpha, iterations, compute_cost, compute_gradient
)
print(f"(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})")
```
Plotting the gradient descent path :
```
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
plt_contour_wgrad(x_train, y_train, p_hist, ax)
```
To observe the effect of a high learning rate:
```
w_init, b_init, iterations = 0, 0, 10
tmp_alpha = 8.0e-1
w_final, b_final, J_hist, p_hist = gradient_descent(
    x_train, y_train, w_init, b_init, tmp_alpha, iterations, compute_cost, compute_gradient
)
plt_divergence(p_hist, J_hist, x_train, y_train)
plt.show()
```
