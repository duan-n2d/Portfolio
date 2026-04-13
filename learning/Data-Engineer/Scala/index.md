---
layout: default
title: "Scala Programming"
---

# 🎯 Scala for Big Data and Functional Programming

Scala is a powerful, modern language for data engineering and distributed computing. It combines object-oriented and functional programming paradigms, making it ideal for building scalable data pipelines with Apache Spark.

## Table of Contents

1. [Why Scala?](#why-scala)
2. [Core Concepts](#core-concepts)
3. [Functional Programming](#functional-programming)
4. [Scala Collections](#scala-collections)
5. [Apache Spark with Scala](#apache-spark-with-scala)
6. [Best Practices](#best-practices)

---

## 🤔 Why Scala?

### Advantages
- **Functional & Object-Oriented**: Best of both worlds
- **Strong Type System**: Catch errors at compile time
- **Concise Syntax**: Less boilerplate than Java
- **Interoperability**: Seamless Java integration
- **Apache Spark**: Official Spark API is Scala
- **Performance**: Compiles to JVM bytecode

### Use Cases
- Real-time data processing with Spark
- Building distributed applications
- ETL pipeline development
- Stream processing

---

## 🎓 Core Concepts

### Variables and Types

```scala
// Immutable variables (preferred)
val name: String = "Data Engineer"
val age: Int = 30

// Mutable variables (use sparingly)
var counter: Int = 0
counter = counter + 1

// Type inference
val salary = 70000  // Int inferred
val rate = 0.05     // Double inferred

// String interpolation
val message = s"Hello, $name! You are $age years old"
val formatted = f"Salary: $salary%.2f"
```

### Functions

```scala
// Simple function
def add(a: Int, b: Int): Int = {
    a + b
}

// Shorthand (single expression)
def multiply(a: Int, b: Int): Int = a * b

// Default parameters
def greet(name: String, greeting: String = "Hello"): String = 
    s"$greeting, $name!"

// Variable arguments
def sum(numbers: Int*): Int = {
    numbers.sum
}

// Higher-order function
def applyTwice(f: Int => Int, x: Int): Int = f(f(x))
applyTwice(x => x * 2, 5)  // 20
```

### Classes and Objects

```scala
// Class definition
class Person(val name: String, val age: Int) {
    def greet(): String = s"Hi, I'm $name"
}

// Object instantiation
val person = new Person("Alice", 30)

// Singleton object
object Config {
    val dbHost = "localhost"
    val dbPort = 5432
}

// Case class (better for data)
case class Employee(name: String, salary: Double) {
    def raiseBy(percent: Double): Employee = 
        copy(salary = salary * (1 + percent))
}
```

---

## 🔄 Functional Programming

### Pure Functions

```scala
// Pure function - same input always produces same output
def calculateBonus(salary: Double): Double = salary * 0.1

// Impure function - depends on external state
var bonusRate = 0.1
def calculateBonusImpure(salary: Double): Double = salary * bonusRate
```

### Immutability

```scala
// Preferred: create new instead of modifying
val original = List(1, 2, 3)
val doubled = original.map(_ * 2)

// Map operations
val numbers = List(1, 2, 3, 4, 5)
numbers.map(x => x * 2)        // [2, 4, 6, 8, 10]
numbers.filter(x => x > 2)     // [3, 4, 5]
numbers.reduce(_ + _)          // 15
```

### Pattern Matching

```scala
// Pattern matching
def describeNumber(n: Int): String = n match {
    case 0 => "Zero"
    case 1 => "One"
    case x if x > 0 => s"Positive: $x"
    case x if x < 0 => s"Negative: $x"
    case _ => "Unknown"
}

// Case class matching
def processData(data: Any): String = data match {
    case Employee(name, salary) => s"$name earns $salary"
    case Person(name, age) => s"$name is $age years old"
    case s: String => s.toUpperCase
    case i: Int => s"Number: $i"
    case _ => "Unknown type"
}
```

---

## 📊 Scala Collections

### Main Collections

```scala
// List - immutable, ordered
val list = List(1, 2, 3, 4, 5)
list.head      // 1
list.tail      // List(2, 3, 4, 5)
list.map(_ * 2) // List(2, 4, 6, 8, 10)

// Set - unique values
val set = Set(1, 2, 2, 3)  // Set(1, 2, 3)
set.contains(2)  // true

// Map - key-value pairs
val map = Map("a" -> 1, "b" -> 2)
map("a")       // 1
map.get("c")   // None

// Tuple - fixed size, mixed types
val tuple = (1, "name", 3.14)
tuple._1       // 1
tuple._2       // "name"
```

### Collection Operations

```scala
val data = List(1, 2, 3, 4, 5)

// Transformation
data.map(_ * 2)           // [2, 4, 6, 8, 10]
data.filter(_ > 2)        // [3, 4, 5]
data.flatMap(x => List(x, x*10))  // [1, 10, 2, 20, ...]

// Aggregation
data.sum                  // 15
data.product              // 120
data.reduce(_ + _)        // 15
data.foldLeft(0)(_ + _)   // 15

// Grouping
data.groupBy(_ % 2)       // Map(1 -> [1,3,5], 0 -> [2,4])

// Sorting
data.sorted              // [1, 2, 3, 4, 5]
data.sortBy(x => -x)     // [5, 4, 3, 2, 1]
```

---

## ⚡ Apache Spark with Scala

### Spark DataFrames

```scala
import org.apache.spark.sql.SparkSession

val spark = SparkSession.builder()
    .appName("DataEngineering")
    .getOrCreate()

// Read data
val df = spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv("data/employees.csv")

// Show data
df.show(10)
df.printSchema()

// Basic operations
df.select("name", "salary")
    .filter($"salary" > 50000)
    .orderBy(desc("salary"))
    .show()
```

### Spark SQL

```scala
df.createOrReplaceTempView("employees")

val result = spark.sql("""
    SELECT 
        department,
        COUNT(*) as emp_count,
        AVG(salary) as avg_salary
    FROM employees
    WHERE salary > 50000
    GROUP BY department
    ORDER BY avg_salary DESC
""")

result.show()
```

### RDD Operations

```scala
// Resilient Distributed Datasets
val rdd = spark.sparkContext.parallelize(List(1, 2, 3, 4, 5))

// Transformations
rdd.map(_ * 2)           // [2, 4, 6, 8, 10]
rdd.filter(_ > 2)        // [3, 4, 5]
rdd.flatMap(x => List(x, x*10))

// Actions
rdd.collect()            // Retrieve all data
rdd.count()              // 5
rdd.first()              // 1
rdd.sum()                // 15
```

---

## ✅ Best Practices

### 1. **Prefer Immutability**
```scala
// Good
val result = data.map(_ * 2)

// Avoid
var result = List[Int]()
for (i <- data) result = result :+ (i * 2)
```

### 2. **Use Pattern Matching**
```scala
// Good
def process(data: Any) = data match {
    case list: List[_] => list.length
    case map: Map[_, _] => map.size
    case _ => "Unknown"
}

// Avoid
def processIf(data: Any) = {
    if (data.isInstanceOf[List[_]]) data.asInstanceOf[List[_]].length
    else if (data.isInstanceOf[Map[_, _]]) data.asInstanceOf[Map[_, _]].size
    else "Unknown"
}
```

### 3. **Leverage Type System**
```scala
// Use proper types
case class Query(table: String, filters: Map[String, String])
def executeQuery(q: Query): DataFrame = ???

// Avoid
def executeQuery(table: String, filters: String): Any = ???
```

### 4. **Functional Composition**
```scala
val pipeline = 
    df.filter($"age" > 18)
      .groupBy("department")
      .agg(avg("salary"), count("*"))
      .orderBy(desc("avg(salary)"))

pipeline.show()
```

### 5. **Error Handling**
```scala
// Using Try-Catch
import scala.util.{Try, Success, Failure}

val result = Try {
    data.map(_ / 0)  // May fail
}

result match {
    case Success(value) => println(s"Result: $value")
    case Failure(exception) => println(s"Error: ${exception.getMessage}")
}

// Using Option
def getValue(map: Map[String, Int], key: String): Option[Int] = 
    map.get(key)

getValue(map, "key").getOrElse(0)
```

---

## 📚 Recommended Resources

- **Scala Official**: [scala-lang.org](https://www.scala-lang.org/)
- **Apache Spark**: [spark.apache.org](https://spark.apache.org/)
- **Functional Programming in Scala**: Excellent book
- **Twitter Scala School**: Free online course
- **Scala by Example**: Martin Odersky's guide

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate to Advanced  
**Prerequisites**: Java or similar programming language, understanding of functional programming concepts

