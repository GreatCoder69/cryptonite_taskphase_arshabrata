import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r"Sample_Datasets\logistic_reg_dataset.csv")  
x = data['Age'].values  
y = data['Purchased'].values 
x = x.reshape(-1, 1)
X = np.c_[np.ones(x.shape[0]), x]  
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
def logistic_regression(X, y, learning_rate, iterations):
    weights = np.zeros(X.shape[1])
    m = len(y)
    for i in range(iterations):
        z = np.dot(X, weights)
        h = sigmoid(z)
        gradient = np.dot(X.T, (h - y)) / m
        weights -= learning_rate * gradient
    return weights
learning_rate = 0.01
iterations = 10000
weights = logistic_regression(X, y, learning_rate, iterations)
print("Weights:", weights)
def predict_purchase(age):
    z = weights[0] + weights[1] * age
    probability = sigmoid(z)
    return probability, 1 if probability >= 0.5 else 0
user_age = float(input("Enter age: "))
probability, purchase_prediction = predict_purchase(user_age)
print(f"Predicted probability of purchase: {probability:.2f}")
if purchase_prediction == 1:
    print("The model predicts that this person has purchased.")
else:
    print("The model predicts that this person has not purchased.")
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, sigmoid(np.dot(X, weights)), color='red', label='Logistic Regression Fit')
plt.scatter(user_age, probability, color='yellow', edgecolor='black', s=100, label='User Input')
plt.xlabel('Age')
plt.ylabel('Probability')
plt.title('Logistic Regression Fit')
plt.legend()
plt.show()
