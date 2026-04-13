---
layout: default
title: "Data Structures"
---

# 🗂️ Data Structures for Data Engineering

Efficient data structures are crucial for building performant data pipelines and systems.

## Essential Data Structures

### Arrays and Lists
- **Fixed Size Array**: O(1) access, fixed memory
- **Dynamic Array**: O(1) amortized insertion, grows as needed

### Linked Lists
- **Singly Linked List**: O(1) insertion/deletion, O(n) access
- **Doubly Linked List**: Bidirectional traversal
- **Circular Linked List**: Last node points to first

### Hash Tables
- **Hash Map**: O(1) average lookup, handling collisions
- **Hash Set**: Unique values, O(1) operations
- **Hash Function**: Maps keys to indices

### Trees
- **Binary Tree**: Each node has 0-2 children
- **Binary Search Tree**: Ordered left < parent < right
- **AVL Tree**: Self-balancing, O(log n) guaranteed
- **B-Tree**: Multi-way tree, optimized for disk access
- **Trie**: Prefix tree for string operations

### Heaps
- **Min-Heap**: Parent <= children
- **Max-Heap**: Parent >= children
- **Operations**: O(log n) insertion/deletion, O(1) peek

### Graphs
- **Adjacency Matrix**: O(1) edge lookup, O(V²) space
- **Adjacency List**: O(E) space, better for sparse graphs

---

## Advanced Structures

### Skip List
- Probabilistic alternative to balanced trees
- O(log n) operations on average
- Simpler implementation than balanced trees

### Bloom Filter
- Probabilistic data structure
- O(1) insertion and lookup
- False positives possible, no false negatives

### Segment Tree
- Efficient range queries and updates
- O(log n) operations
- Used in competitive programming

### Balanced BSTs
- **Red-Black Tree**: Path-balanced
- **AVL Tree**: Height-balanced
- **Splay Tree**: Recently accessed items fast

---

## Choosing the Right Structure

| Task | Best Structure | Time |
|------|---|---|
| Fast lookup | Hash Table | O(1) |
| Sorted access | BST | O(log n) |
| Priority queue | Heap | O(log n) |
| Prefix search | Trie | O(k) |
| Range queries | Segment Tree | O(log n) |
| Set operations | Bloom Filter | O(1) |

---

## Implementation Considerations

### Memory Usage
- Avoid unnecessary copying
- Use references instead of values
- Consider cache locality for performance

### Time Complexity
- Analyze worst, average, best cases
- Amortized analysis for dynamic structures
- Trade-off between space and time

### Practical Tips
1. Use built-in data structures (Python lists, dicts)
2. Understand underlying implementations
3. Choose based on access patterns
4. Profile before optimizing
5. Document assumptions

---

**Last updated**: April 12, 2026  
**Difficulty**: Intermediate  
**Prerequisites**: Basic programming
