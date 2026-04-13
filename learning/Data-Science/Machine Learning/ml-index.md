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
- Gradient Boosting: Powerful ensemble method (XGBoost, LightGBM)
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

**Common Classification Algorithms:**
- Logistic Regression: Simple, interpretable baseline
- Decision Trees: Interpretable, handles non-linearity
- Random Forest: Ensemble method, reduces overfitting
- Gradient Boosting: High performance
- Support Vector Machines: Effective in high dimensions
- Naive Bayes: Fast, works well with text
- Neural Networks: Complex patterns, requires more data

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

# Visualization
plt.scatter(X[:, 0], X[:, 1], c=clusters, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
            c='red', marker='X', s=200)
plt.title('K-Means Clustering')
plt.show()
```

**Common Clustering Algorithms:**
- K-Means: Fast, simple, assumes spherical clusters
- Hierarchical Clustering: Dendrogram visualization
- DBSCAN: Density-based, handles irregular shapes
- Gaussian Mixture Models: Probabilistic clusters

### Dimensionality Reduction

Reducing feature space while preserving information.

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import pandas as pd

# Load data
X, y = load_iris(return_X_y=True)

# PCA - keep 2 components
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"Total variance explained: {sum(pca.explained_variance_ratio_):.2%}")
```

**Common Dimensionality Reduction Techniques:**
- Principal Component Analysis (PCA): Linear, preserves variance
- t-SNE: Non-linear, good for visualization
- UMAP: Better for structure preservation
- Autoencoders: Deep learning approach

---

## 📈 Model Evaluation

### Train-Test Split

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

**Key Parameters:**
- `test_size`: Proportion of data for testing (typically 0.2)
- `random_state`: For reproducibility
- `stratify`: Maintains class distribution (important for classification)

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.4f}, Std: {scores.std():.4f}")
```

### Classification Metrics

```python
from sklearn.metrics import confusion_matrix, classification_report

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Detailed report
print(classification_report(y_test, y_pred))

# Metrics for binary classification
from sklearn.metrics import roc_auc_score, roc_curve

auc = roc_auc_score(y_test, y_pred_proba)
```

**Important Metrics:**
- **Accuracy**: (TP + TN) / Total - when classes are balanced
- **Precision**: TP / (TP + FP) - when false positives are costly
- **Recall/Sensitivity**: TP / (TP + FN) - when false negatives are costly
- **F1-Score**: Harmonic mean of precision and recall
- **ROC-AUC**: Measures trade-off between TPR and FPR

### Regression Metrics

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
```

---

## ⚙️ Hyperparameter Tuning

### Grid Search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

model = RandomForestClassifier()
grid_search = GridSearchCV(model, param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

print(f"Best params: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")
```

### Random Search

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': [5, 10, 15, None],
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(model, param_dist, cv=5, n_iter=20, n_jobs=-1)
random_search.fit(X_train, y_train)
```

---

## ✅ Best Practices

### 1. **Data Preprocessing**
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Never fit scaler on test data!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Only transform!
```

### 2. **Avoid Data Leakage**
- Don't preprocess before splitting
- Don't use test set information during training
- Scale separately for train and test

### 3. **Handle Imbalanced Data**
```python
from sklearn.utils.class_weight import compute_class_weight

# Option 1: Adjust class weights
weights = compute_class_weight('balanced', np.unique(y_train), y_train)
model.fit(X_train, y_train, sample_weight=weights)

# Option 2: Use SMOTE
from imblearn.over_sampling import SMOTE
smote = SMOTE()
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)
```

### 4. **Feature Engineering**
```python
# Create new features based on domain knowledge
df['age_squared'] = df['age'] ** 2
df['log_income'] = np.log(df['income'])

# Interaction features
df['age_income_interaction'] = df['age'] * df['income']
```

### 5. **Model Interpretability**
```python
# Feature importance (for tree-based models)
feature_importance = model.feature_importances_
sorted_idx = np.argsort(feature_importance)[::-1]

# SHAP for model-agnostic explanations
import shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
```

---

## 📚 Recommended Resources

- **Scikit-learn Documentation**: [scikit-learn.org](https://scikit-learn.org/)
- **Andrew Ng's ML Course**: Excellent foundational course
- **Kaggle Competitions**: Real-world ML problems
- **Papers with Code**: Browse ML research papers with implementations

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate to Advanced  
**Prerequisites**: Python, NumPy, Pandas basics