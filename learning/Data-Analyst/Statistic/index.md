---
layout: default
title: "Statistical Analysis"
---

# 📊 Statistical Analysis for Data Professionals

Statistical thinking is fundamental to data analysis. Master hypothesis testing, distributions, and statistical inference to derive meaningful insights from data.

## Descriptive Statistics

### Central Tendency
- **Mean**: Average value
- **Median**: Middle value (robust to outliers)
- **Mode**: Most frequent value

### Dispersion
- **Variance**: Measure of spread
- **Standard Deviation**: Square root of variance
- **Range**: Max - Min
- **IQR**: Interquartile range (Q3 - Q1)

```python
import numpy as np
import scipy.stats as stats

data = [1, 2, 2, 3, 4, 5, 5, 5, 6, 100]

# Summary statistics
mean = np.mean(data)
median = np.median(data)
std = np.std(data)
variance = np.var(data)

# Percentiles
q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)
```

## Probability Distributions

### Normal Distribution
- Bell-shaped, symmetric
- 68-95-99.7 rule
- Most common in nature

### Poisson Distribution
- Count data, rare events
- Events at fixed rate
- Example: Email arrivals, bugs per code

### Binomial Distribution
- Success/failure outcomes
- Fixed number of trials
- Example: Customer churn

```python
from scipy.stats import norm, poisson, binom

# Normal distribution
prob = norm.cdf(100, loc=100, scale=15)  # P(X <= 100)

# Poisson distribution
prob = poisson.pmf(5, mu=3)  # P(X = 5 | λ = 3)

# Binomial distribution
prob = binom.pmf(3, n=10, p=0.5)  # P(X = 3)
```

## Hypothesis Testing

### Null Hypothesis (H₀) vs Alternative Hypothesis (H₁)
- H₀: No effect or no difference
- H₁: There is an effect or difference

### P-value
- Probability of observing result if H₀ is true
- **p < 0.05**: Typically reject H₀ (statistically significant)
- **p >= 0.05**: Fail to reject H₀

```python
from scipy.stats import ttest_ind, chi2_contingency

# Two-sample t-test (comparing means)
t_stat, p_value = ttest_ind(group1, group2)

# Chi-square test (categorical data)
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

# Interpretation
if p_value < 0.05:
    print("Result is statistically significant")
else:
    print("Result is not statistically significant")
```

## Correlation and Causation

### Correlation Coefficients
- **Pearson**: -1 (perfect negative) to +1 (perfect positive)
- **Spearman**: Rank correlation, robust to outliers
- **Kendall**: Another rank correlation

```python
from scipy.stats import pearsonr, spearmanr

# Pearson correlation
corr, p_value = pearsonr(x, y)

# Spearman correlation (for non-linear relationships)
corr, p_value = spearmanr(x, y)
```

### Important Note
⚠️ **Correlation ≠ Causation**  
- Confounding variables
- Reverse causality
- Coincidence

## Time Series Analysis

### Trend, Seasonality, Residuals
- Decompose time series into components
- Identify patterns
- Forecast future values

```python
from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(timeseries, model='additive', period=12)
trend = result.trend
seasonality = result.seasonal
residual = result.resid
```

---

## Practice Tips

1. **Calculate confidence intervals** for estimates
2. **Check assumptions** before tests (normality, equal variance)
3. **Use effect size** alongside p-values
4. **Create visualizations** (histograms, Q-Q plots, scatter plots)
5. **Document assumptions** and limitations

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate  
**Prerequisites**: Basic math knowledge
