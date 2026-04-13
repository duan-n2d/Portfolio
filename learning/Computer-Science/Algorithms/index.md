---
layout: default
title: "Algorithms & Data Structures"
---

# 🧮 Algorithms & Data Structures

Master fundamental algorithms and data structures. These are essential building blocks for solving coding problems efficiently and architecting scalable systems.

## Core Data Structures

### Arrays & Lists
- Dynamic resizing, O(1) access, O(n) insertion
- Use for sequential access and lookups

### Linked Lists
- O(1) insertion/deletion, O(n) access
- Use for insertion-heavy operations

### Hash Tables / Dictionaries
- O(1) average lookup, insertion, deletion
- Foundation for caching and indexing

### Trees
- **Binary Search Trees**: Ordered access, O(log n) operations
- **Balanced Trees (AVL, Red-Black)**: Guarantee O(log n)
- **Heap**: Priority queue implementation

### Graphs
- Vertices and edges
- Representations: Adjacency matrix, adjacency list

---

## Fundamental Algorithms

### Sorting

**Merge Sort**: O(n log n) guaranteed, stable
```
Divide-and-conquer approach
Time: O(n log n), Space: O(n)
```

**Quick Sort**: O(n log n) average, O(n²) worst
```
Divide-and-conquer, in-place
Time: O(n log n) avg, Space: O(log n)
```

**Heap Sort**: O(n log n) guaranteed, in-place
```
Uses heap structure
Time: O(n log n), Space: O(1)
```

### Searching

**Binary Search**: O(log n)
```
Sorted array only
Divide search space by half each iteration
```

**Hash Table Lookup**: O(1) average
```
Constant time access with good hash function
```

### Graph Algorithms

**Breadth-First Search (BFS)**: O(V + E)
```
Level-by-level traversal, finds shortest path in unweighted
Use for: Level order traversal, shortest path
```

**Depth-First Search (DFS)**: O(V + E)
```
Recursive or stack-based traversal
Use for: Topological sort, cycle detection
```

**Dijkstra's Algorithm**: O((V + E) log V)
```
Shortest path in weighted graphs (non-negative weights)
Greedy approach with priority queue
```

---

## Algorithmic Paradigms

### Dynamic Programming
Solve subproblems and combine results
Example: Fibonacci, Longest Common Subsequence, Knapsack

### Greedy Algorithms
Make locally optimal choices
Example: Activity Selection, Huffman Coding

### Divide and Conquer
Break problem into subproblems
Example: Merge Sort, Quick Sort, Binary Search

### Backtracking
Explore all possibilities with pruning
Example: N-Queens, Sudoku Solver

---

## Complexity Analysis

### Big O Notation

**O(1)** - Constant time  
**O(log n)** - Logarithmic  
**O(n)** - Linear  
**O(n log n)** - Linearithmic  
**O(n²)** - Quadratic  
**O(n³)** - Cubic  
**O(2ⁿ)** - Exponential  
**O(n!)** - Factorial  

### When to Use Each Complexity
- For 10⁶ elements: O(n) or O(n log n) needed
- For 10³ elements: O(n²) acceptable
- For 20 elements: O(2ⁿ) might work

---

## Python Implementation Tips

```python
# Use built-in data structures efficiently
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

# Sorting
sorted(arr)  # O(n log n)
arr.sort()   # In-place, O(n log n)

# Binary search
import bisect
bisect.bisect_left(arr, target)  # Find insertion point

# Graph representation
graph = defaultdict(list)  # Adjacency list

# Priority queue (min-heap)
heap = []
heappush(heap, (priority, value))
priority, value = heappop(heap)
```

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate  
**Prerequisites**: Basic programming knowledge
