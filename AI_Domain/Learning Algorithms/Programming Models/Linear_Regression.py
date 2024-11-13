import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r"Sample_Datasets\linear_reg_dataset.csv")
features = data.iloc[:, :-1].values
target = data.iloc[:, -1].values
feature_names = data.columns[:-1].tolist()
df = pd.DataFrame(features, columns=feature_names)
correlation_matrix = df.corr()
np.fill_diagonal(correlation_matrix.values, 0) 
sorted_correlation = correlation_matrix.unstack().sort_values(ascending=False, key=abs)
dataset = np.hstack((features, target.reshape(-1, 1)))
np.random.shuffle(dataset)
X = dataset[:, :-1]
y = dataset[:, -1]
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X = (X - X_mean) / X_std
train_size = 170
test_size = 30
X_train, y_train = X[:train_size], y[:train_size]
X_test, y_test = X[train_size:], y[train_size:]
X_train = np.hstack((np.ones((train_size, 1)), X_train))
X_test = np.hstack((np.ones((test_size, 1)), X_test))
num_features = X.shape[1]
weights = np.zeros(num_features + 1)
learning_rate = 0.01
convergence_threshold = 1e-6
prev_cost = float("inf")
while True:
    predictions = X_train @ weights
    errors = y_train - predictions
    weights += (learning_rate / train_size) * (X_train.T @ errors)
    current_cost = (1 / (2 * train_size)) * np.sum(errors**2)
    if abs(current_cost - prev_cost) <= convergence_threshold:
        break
    prev_cost = current_cost
y_pred = X_test @ weights
plt.scatter(y_test, y_pred, alpha=0.5, label="Predicted vs Actual")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", label="Ideal Fit")
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Values")
plt.legend()
plt.show()
