import numpy as np
import pandas as pd
import random
from collections import Counter
def normalize_dataset(dataset):
    normalized_data = []
    features = np.array(dataset)[:, :-1]  
    min_vals = np.min(features, axis=0)
    max_vals = np.max(features, axis=0)
    ranges = max_vals - min_vals
    for row in dataset:
        normalized_features = (row[:-1] - min_vals) / ranges
        normalized_data.append(np.append(normalized_features, row[-1]))
    return normalized_data
def remove_outliers(dataset):
    features = np.array(dataset)[:, :-1] 
    mean = np.mean(features, axis=0)
    std_dev = np.std(features, axis=0)
    cleaned_data = []
    for row in dataset:
        z_scores = (row[:-1] - mean) / std_dev
        if all(np.abs(z_scores) < 3): 
            cleaned_data.append(row)
    return cleaned_data
def k_nearest_neighbors(data, predict, k=3):   
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    distances = sorted(distances)[:k]
    weights = [1 / d[0] if d[0] != 0 else 1 for d in distances] 
    weighted_votes = {}
    for i, (_, group) in enumerate(distances):
        weighted_votes[group] = weighted_votes.get(group, 0) + weights[i]
    votes_result = max(weighted_votes, key=weighted_votes.get)
    confidence = (weighted_votes[votes_result] / sum(weights)) * 100
    return votes_result, confidence
def cross_validate(dataset, k, folds=5):
    fold_size = len(dataset) // folds
    accuracies = []
    for i in range(folds):
        train_data = dataset[:i * fold_size] + dataset[(i + 1) * fold_size:]
        test_data = dataset[i * fold_size:(i + 1) * fold_size]
        train_set = {cls: [] for cls in set(row[-1] for row in dataset)}
        test_set = {cls: [] for cls in set(row[-1] for row in dataset)}
        for row in train_data:
            train_set[row[-1]].append(row[:-1])
        for row in test_data:
            test_set[row[-1]].append(row[:-1])
        correct = 0
        total = 0
        for group in test_set:
            for data in test_set[group]:
                vote, _ = k_nearest_neighbors(train_set, data, k=k)
                if group == vote:
                    correct += 1
                total += 1
        accuracies.append(correct / total)
    return sum(accuracies) / len(accuracies)
if __name__ == "__main__":
    df = pd.read_csv(r"Sample_Datasets\knn_dataset.csv")
    df.replace('?', np.nan, inplace=True)
    df.dropna(inplace=True)
    class_column = df.columns[-1]
    full_data = df.astype(float).values.tolist()
    full_data = remove_outliers(full_data)
    full_data = normalize_dataset(full_data)
    random.shuffle(full_data)
    test_size = 0.1
    train_set = {cls: [] for cls in set(row[-1] for row in full_data)}
    test_set = {cls: [] for cls in set(row[-1] for row in full_data)}
    training_data = full_data[:-int(test_size * len(full_data))]
    testing_data = full_data[-int(test_size * len(full_data)):]
    for row in training_data:
        train_set[row[-1]].append(row[:-1])  
    for row in testing_data:
        test_set[row[-1]].append(row[:-1])  
    best_k = 1
    best_accuracy = 0
    for k in range(1, 11):  
        accuracy = cross_validate(full_data, k=k, folds=5)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k
    correct = 0
    total = 0
    for group in test_set:
        for data in test_set[group]:
            vote, confidence = k_nearest_neighbors(train_set, data, k=best_k)
            if group == vote:
                correct += 1
            total += 1
    print(f"Test Set Accuracy: {(correct / total) * 100:.2f}%")
