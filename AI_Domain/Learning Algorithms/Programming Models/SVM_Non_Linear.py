import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"Sample_Datasets\svm_nonlinear_data.csv") 
X = data[['Feature_1', 'Feature_2']].values 
y = data['Label'].values 
y = np.where(y == 1, 1, -1)
def rbf_kernel(x1, x2, sigma=1.0):
    return np.exp(-np.linalg.norm(x1 - x2)**2 / (2 * (sigma ** 2)))
def compute_gram_matrix(X, sigma=1.0):
    m = X.shape[0]
    K = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            K[i, j] = rbf_kernel(X[i], X[j], sigma)
    return K
def train_svm(X, y, C=1.0, sigma=1.0, lr=0.001, epochs=1000):
    m, n = X.shape
    alpha = np.zeros(m) 
    b = 0 
    K = compute_gram_matrix(X, sigma)
    for epoch in range(epochs):
        for i in range(m):
            prediction = np.sum(alpha * y * K[:, i]) + b
            if y[i] * prediction < 1:
                alpha[i] += lr * (1 - y[i] * prediction)
                alpha[i] = min(max(alpha[i], 0), C)
                b += lr * y[i]
    return alpha, b
def predict(X_train, y_train, alpha, b, X_test, sigma=1.0):
    K_test = np.array([np.sum(alpha * y_train * [rbf_kernel(x, x_train, sigma) for x_train in X_train]) for x in X_test])
    return np.sign(K_test + b)
alpha, b = train_svm(X, y, C=1.0, sigma=0.5, lr=0.001, epochs=1000)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
grid = np.c_[xx.ravel(), yy.ravel()]
Z = predict(X, y, alpha, b, grid, sigma=0.5)
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.2, colors=['red', 'green'])
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', edgecolor='k')
plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Non-linear SVM Decision Boundary with RBF Kernel')
plt.show()
