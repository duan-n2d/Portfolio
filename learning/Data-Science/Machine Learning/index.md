---
layout: default
title: "Machine Learning"
---

# 🤖 Machine Learning Fundamentals

Machine Learning enables systems to learn from data and make predictions without being explicitly programmed. This guide covers essential ML concepts from theory to practice.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Supervised Learning](#supervised-learning)
3. [Unsupervised Learning](#unsupervised-learning)
4. [Model Evaluation](#model-evaluation)
5. [Best Practices](#best-practices)

---

## 🎯 Core Concepts

### What is Machine Learning?

Machine Learning is a subset of Artificial Intelligence that enables systems to learn and improve from experience without being explicitly programmed.

**Three Main Types:**
- **Supervised Learning**: Learning from labeled data (classification, regression)
- **Unsupervised Learning**: Finding patterns in unlabeled data (clustering, dimensionality reduction)
- **Reinforcement Learning**: Learning through interaction with an environment

### The ML Workflow

```
1. Problem Definition
        ↓
2. Data Collection & Exploration (EDA)
        ↓
3. Data Preprocessing & Feature Engineering
        ↓
4. Model Selection
        ↓
5. Model Training
        ↓
6. Evaluation & Validation
        ↓
7. Hyperparameter Tuning
        ↓
8. Deployment & Monitoring
```

### Key Concepts

**Features (X)**: Input variables used to make predictions  
**Target (y)**: The value we're trying to predict  
**Training Set**: Data used to train the model  
**Validation Set**: Data used to tune hyperparameters  
**Test Set**: Data used to evaluate final model performance  

---

## 📊 Supervised Learning

### Regression

Predicting continuous numerical values.

```python
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse:.4f}, R²: {r2:.4f}")
```

**Common Regression Algorithms:**
- Linear Regression: Simple, interpretable baseline
- Ridge/Lasso Regression: Regression with regularization
- Decision Trees: Non-linear patterns
- Random Forest: Ensemble of decision trees
- Gradient Boosting: Powerful ensemble method
- Support Vector Regression: Kernel-based regression

### Classification

Predicting categorical values.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.4f}")
print(f"F1-Score: {f1_score(y_test, y_pred, average='weighted'):.4f}")
```

---

## 🔍 Unsupervised Learning

### Clustering

Grouping similar data points together.

```python
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generate sample data
X, _ = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)

# K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
clusters = kmeans.fit_predict(X)
```

### Dimensionality Reduction

Reducing feature space while preserving information.

```python
from sklearn.decomposition import PCA

# PCA - keep 2 components
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Explained variance: {sum(pca.explained_variance_ratio_):.2%}")
```

---

## 📈 Model Evaluation

### Important Metrics

- **Accuracy**: (TP + TN) / Total
- **Precision**: TP / (TP + FP)
- **Recall**: TP / (TP + FN)
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Trade-off between TPR and FPR

---

## ✅ Best Practices

1. **Never fit scaler on test data**
2. **Always stratify when splitting classification data**
3. **Use cross-validation for robust evaluation**
4. **Handle imbalanced data appropriately**
5. **Feature engineering based on domain knowledge**

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate to Advanced
