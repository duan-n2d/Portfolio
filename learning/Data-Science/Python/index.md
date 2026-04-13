---
layout: default
title: "Python for Data Science"
---

# 🐍 Python Fundamentals for Data Science

Python has become the de-facto language for data science, machine learning, and data engineering. This comprehensive guide covers essential Python concepts tailored for data professionals.

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Essential Libraries](#essential-libraries)
3. [Data Manipulation](#data-manipulation)
4. [Visualization](#visualization)
5. [Best Practices](#best-practices)

---

## 🎯 Core Concepts

### Variables and Data Types

Python's dynamic typing makes it flexible for data work:

```python
# Numbers
integer = 42
floating_point = 3.14
complex_num = 2 + 3j

# Strings (immutable)
name = "Data Engineer"
text = f"Hello, {name}!"  # f-strings are preferred

# Booleans
is_valid = True
has_data = False

# None (null-like value)
result = None
```

**Key Point**: Python's type flexibility comes with responsibility—always validate data types when working with external inputs.

### Collections

```python
# List - ordered, mutable, allows duplicates
numbers = [1, 2, 3, 4, 5]
mixed = [1, "text", 3.14, True]

# Tuple - ordered, immutable, allows duplicates
coordinates = (10.5, 20.3)

# Dictionary - key-value pairs, mutable
user = {"name": "John", "age": 30, "role": "Engineer"}

# Set - unordered, unique values, mutable
unique_tags = {"python", "data", "engineering"}
```

### Operators and Control Flow

```python
# Comparison operators
x = 10
print(x > 5)   # True
print(x == 10)  # True
print(x != 5)   # True

# Logical operators
if x > 5 and x < 20:
    print("x is between 5 and 20")
elif x <= 5:
    print("x is 5 or less")
else:
    print("x is greater than 20")

# Loops
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

numbers = [1, 2, 3, 4, 5]
while numbers:
    print(numbers.pop())
```

---

## 📚 Essential Libraries

### NumPy - Numerical Computing

NumPy is the foundation of scientific computing in Python:

```python
import numpy as np

# Create arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
print(arr.mean())     # 3.0
print(arr.std())      # Standard deviation
print(np.sum(arr))    # 15

# Element-wise operations
arr2 = arr * 2
arr3 = arr + 10

# Linear algebra
np.dot(matrix, matrix.T)  # Matrix multiplication
```

**Use Case**: NumPy is essential for mathematical computations and forms the backbone of pandas and scikit-learn.

### Pandas - Data Manipulation

Pandas is your primary tool for data manipulation:

```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'salary': [50000, 60000, 75000]
})

# Data inspection
print(df.head())
print(df.info())
print(df.describe())

# Data selection
print(df['name'])
print(df[df['age'] > 25])

# Data transformation
df['bonus'] = df['salary'] * 0.1
df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 100], labels=['Young', 'Mid', 'Senior'])
```

**Best Practice**: Always use `df.head()`, `df.info()`, and `df.describe()` when starting to work with a new dataset.

### Scikit-learn - Machine Learning

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train_scaled, y_train)

# Evaluate
score = model.score(X_test_scaled, y_test)
```

---

## 🔄 Data Manipulation Patterns

### Reading and Writing Data

```python
import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')

# Read Excel
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Read JSON
df = pd.read_json('data.json')

# Write to CSV
df.to_csv('output.csv', index=False)

# Write to Excel
df.to_excel('output.xlsx', index=False)
```

### Handling Missing Data

```python
# Check for missing values
print(df.isnull().sum())

# Drop missing values
df_clean = df.dropna()

# Fill missing values
df['age'].fillna(df['age'].mean(), inplace=True)

# Forward/backward fill for time series
df['value'].fillna(method='ffill')
```

### Grouping and Aggregation

```python
# Group and aggregate
grouped = df.groupby('department').agg({
    'salary': ['mean', 'sum', 'count'],
    'age': 'mean'
})

# Using apply for custom functions
def classify_age(age):
    if age < 30:
        return 'Young'
    elif age < 50:
        return 'Middle'
    else:
        return 'Senior'

df['age_class'] = df['age'].apply(classify_age)
```

### Joining and Merging

```python
# Merge DataFrames
result = pd.merge(df1, df2, on='id', how='inner')

# Concatenate
combined = pd.concat([df1, df2], axis=0)
```

---

## 📊 Visualization

### Matplotlib - Static Plots

```python
import matplotlib.pyplot as plt

# Line plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Data', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.legend()
plt.grid(True)
plt.show()

# Histogram
plt.hist(data, bins=30, edgecolor='black')
plt.show()
```

### Seaborn - Statistical Visualization

```python
import seaborn as sns

# Boxplot
sns.boxplot(data=df, x='category', y='value')

# Scatterplot
sns.scatterplot(data=df, x='age', y='salary', hue='department')

# Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
```

---

## ✅ Best Practices

### 1. **Code organization**
```python
# Group imports at the top
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Use clear variable names
customer_data = pd.read_csv('customers.csv')
```

### 2. **Error handling**
```python
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("File not found!")
except pd.errors.ParserError:
    print("Error parsing CSV!")
```

### 3. **List comprehensions**
```python
# More efficient than loops
squares = [x**2 for x in range(10)]

# With conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### 4. **Functions and modularity**
```python
def preprocess_data(df):
    """
    Clean and preprocess data.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Preprocessed DataFrame
    """
    df = df.dropna()
    df['value'] = df['value'].astype(float)
    return df
```

### 5. **Performance tips**
```python
# Use vectorized operations instead of loops
# ✓ Good
df['new_col'] = df['col1'] * df['col2']

# ✗ Slow
for i in range(len(df)):
    df.loc[i, 'new_col'] = df.loc[i, 'col1'] * df.loc[i, 'col2']
```

---

## 📚 Recommended Resources

- **Official Documentation**: [Python.org](https://www.python.org/)
- **Pandas**: [pandas.pydata.org](https://pandas.pydata.org/)
- **NumPy**: [numpy.org](https://numpy.org/)
- **Scikit-learn**: [scikit-learn.org](https://scikit-learn.org/)
- **Real Python**: Comprehensive tutorials on Python topics

---

**Last updated**: April 12, 2026  
**Difficulty**: Beginner to Intermediate  
**Prerequisites**: Basic programming knowledge

