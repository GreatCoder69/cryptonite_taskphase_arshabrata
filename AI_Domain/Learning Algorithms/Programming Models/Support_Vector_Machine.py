import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"Sample_Datasets\svm_linear_dataset.csv")
X = data[['x1', 'x2']].values
Y = data['label'].values
for i in range(len(X)):
    if Y[i] == -1:
        plt.scatter(X[i][0], X[i][1], s=30, color='green', marker='o', linewidths=2)
    else:
        plt.scatter(X[i][0], X[i][1], s=30, color='red', marker='o', linewidths=2)
learning_rate = 0.001
epochs = 10000
C = 1 
w = np.zeros(len(X[0]))
b = 0
def train_svm(X, Y, learning_rate, epochs, C):
    global w, b
    for epoch in range(epochs):
        for i in range(len(X)):
            if Y[i] * (np.dot(X[i], w) + b) < 1:
                w = w + learning_rate * (X[i] * Y[i] + (-2 * (1 / epochs) * w))
                b = b + learning_rate * Y[i]
            else:
                w = w + learning_rate * (-2 * (1 / epochs) * w)
    return w, b
w, b = train_svm(X, Y, learning_rate, epochs, C)
print("Weights:", w)
print("Bias:", b)
x1 = np.linspace(min(X[:, 0]) - 1, max(X[:, 0]) + 1, 100)
x2 = - (w[0] * x1 + b) / w[1]
plt.plot(x1, x2, 'r-', label="Decision Boundary")
margin = 1 / np.sqrt(np.sum(w ** 2))
x2_positive_margin = x2 + margin
x2_negative_margin = x2 - margin
plt.plot(x1, x2_positive_margin, 'b--', label="Positive Margin")
plt.plot(x1, x2_negative_margin, 'g--', label="Negative Margin")
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend()
plt.title("SVM Decision Boundary with Margins")
plt.show()
