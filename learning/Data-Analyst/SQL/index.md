---
layout: default
title: "SQL Mastery"
---

# 📊 SQL Mastery for Data Analysis

SQL is the universal language for data analysis and business intelligence. Master SQL to unlock the power of relational databases and become proficient in data querying, manipulation, and transformation.

## Table of Contents

1. [SQL Fundamentals](#sql-fundamentals)
2. [Querying Data](#querying-data)
3. [Advanced Concepts](#advanced-concepts)
4. [Optimization](#optimization)
5. [Best Practices](#best-practices)

---

## 🎯 SQL Fundamentals

### Basic SELECT Statement

```sql
-- Simple query
SELECT name, salary, department 
FROM employees 
WHERE salary > 50000 
ORDER BY salary DESC 
LIMIT 10;

-- Select all columns
SELECT * FROM employees;

-- Select with alias
SELECT 
    emp_id AS employee_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    salary * 12 AS annual_salary
FROM employees;
```

### WHERE Clause Operators

```sql
-- Comparison operators
SELECT * FROM employees WHERE age > 30;
SELECT * FROM employees WHERE salary != 50000;
SELECT * FROM employees WHERE hire_date >= '2020-01-01';

-- Logical operators
SELECT * FROM employees 
WHERE department = 'Sales' AND salary > 60000;

SELECT * FROM employees 
WHERE department IN ('Sales', 'Marketing', 'IT');

SELECT * FROM employees 
WHERE name LIKE '%Smith%';
```

### Basic Aggregation

```sql
-- Count rows
SELECT COUNT(*) AS total_employees FROM employees;

-- Aggregate functions
SELECT 
    COUNT(*) AS employee_count,
    AVG(salary) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    SUM(salary) AS total_salary
FROM employees;

-- Group By
SELECT 
    department,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 5
ORDER BY avg_salary DESC;
```

---

## 🔍 Querying Data

### Joins

```sql
-- INNER JOIN - only matching records
SELECT 
    e.name,
    e.salary,
    d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN - all from left table
SELECT 
    e.name,
    d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Multiple Joins
SELECT 
    e.name,
    d.dept_name,
    p.project_name
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id
INNER JOIN projects p ON e.emp_id = p.assigned_to;
```

### Subqueries

```sql
-- Subquery in WHERE
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in FROM
SELECT department, avg_sal FROM (
    SELECT department, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department
) dept_avg
WHERE avg_sal > 50000;

-- Correlated subquery
SELECT e.name, e.salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary) 
    FROM employees 
    WHERE department = e.department
);
```

### Window Functions

```sql
-- ROW_NUMBER
SELECT 
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS sal_rank
FROM employees;

-- Partition By
SELECT 
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- Running total
SELECT 
    date,
    revenue,
    SUM(revenue) OVER (ORDER BY date) AS running_total
FROM sales
ORDER BY date;
```

---

## 🚀 Advanced Concepts

### Common Table Expressions (CTE)

```sql
-- Single CTE
WITH high_earners AS (
    SELECT emp_id, name, salary
    FROM employees
    WHERE salary > 80000
)
SELECT * FROM high_earners;

-- Multiple CTEs
WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department
),
high_earners AS (
    SELECT e.name, e.salary, d.avg_salary
    FROM employees e
    INNER JOIN dept_avg d ON e.department = d.department
    WHERE e.salary > d.avg_salary
)
SELECT * FROM high_earners;
```

### Union and Combine Results

```sql
-- UNION removes duplicates
SELECT name FROM employees
UNION
SELECT name FROM contractors;

-- UNION ALL keeps duplicates
SELECT name FROM employees
UNION ALL
SELECT name FROM contractors;

-- INTERSECT - common records
SELECT name FROM employees
INTERSECT
SELECT name FROM contractors;
```

### Conditional Logic

```sql
-- CASE statement
SELECT 
    name,
    salary,
    CASE 
        WHEN salary < 40000 THEN 'Junior'
        WHEN salary < 70000 THEN 'Mid'
        WHEN salary < 100000 THEN 'Senior'
        ELSE 'Executive'
    END AS salary_level
FROM employees;

-- Multiple conditions
SELECT 
    name,
    department,
    CASE 
        WHEN department = 'Sales' AND salary > 60000 THEN 'High Performer'
        WHEN department = 'Sales' THEN 'Sales'
        ELSE 'Other'
    END AS classification
FROM employees;
```

---

## ⚡ Optimization

### Indexing

```sql
-- Create index
CREATE INDEX idx_emp_dept ON employees(department);

-- Multi-column index
CREATE INDEX idx_emp_dept_salary ON employees(department, salary);

-- Drop index
DROP INDEX idx_emp_dept;
```

### Query Performance

```sql
-- Use EXPLAIN to analyze query plan
EXPLAIN SELECT * FROM employees WHERE department = 'Sales';

-- Avoid SELECT *
SELECT emp_id, name, salary FROM employees;  -- Better

-- Use appropriate data types
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);
```

### Aggregation Optimization

```sql
-- Inefficient: Subquery in SELECT
SELECT 
    name,
    (SELECT COUNT(*) FROM orders WHERE emp_id = e.emp_id) AS order_count
FROM employees e;

-- Better: Use Join with aggregation
SELECT 
    e.name,
    COUNT(o.order_id) AS order_count
FROM employees e
LEFT JOIN orders o ON e.emp_id = o.emp_id
GROUP BY e.emp_id, e.name;
```

---

## ✅ Best Practices

### 1. **Always use column aliases for clarity**
```sql
SELECT 
    emp_id AS employee_id,
    concat(first_name, ' ', last_name) AS full_name
FROM employees;
```

### 2. **Format queries for readability**
```sql
-- Good formatting
SELECT 
    e.name,
    d.department_name,
    COUNT(o.order_id) AS order_count
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN orders o ON e.emp_id = o.emp_id
GROUP BY e.emp_id, e.name, d.department_name
ORDER BY order_count DESC;
```

### 3. **Use parameterized queries to prevent SQL injection**
```sql
-- Poor (vulnerable)
SELECT * FROM users WHERE email = '" + userInput + "'

-- Better (use parameters)
SELECT * FROM users WHERE email = ?  -- Parameter binding
```

### 4. **Understand NULL handling**
```sql
-- NULL comparisons
SELECT * FROM users WHERE phone IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;

-- NULL in aggregations
SELECT COUNT(phone) FROM users;  -- Excludes NULLs
SELECT COUNT(*) FROM users;     -- Includes NULLs
```

### 5. **Document complex queries**
```sql
-- Calculate monthly sales by region
-- Excludes cancelled orders and adjusted for returns
SELECT 
    region,
    DATE_TRUNC('month', order_date) AS month,
    SUM(total_amount) AS monthly_sales
FROM orders
WHERE status != 'CANCELLED' AND return_status IS NULL
GROUP BY region, DATE_TRUNC('month', order_date)
ORDER BY month DESC;
```

---

## 📚 Resources

- **SQL Documentation**: Database-specific (MySQL, PostgreSQL, SQL Server)
- **LeetCode**: SQL practice problems
- **Mode Analytics**: SQL Tutorial & Editor
- **Use EXPLAIN**: Analyze and optimize your queries

---

**Last updated**: April 12, 2026  
**Difficulty**: Beginner to Advanced  
**Prerequisites**: Basic database concepts
