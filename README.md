# Cracking-The-Coding-Interview

This repository contains code for common data structures and algorthms in Python to help with cracking the coding interview, specifically for the Data Engineer role. The topics discussed here have been collected from various sources including Cracking the Coding Interview (6th Edition) by Gayle Laakmann McDowell. The motivation behind this project is to:

- Improving my own skills on key topics of data structures and algorithms
- Provide a reference to others preparing for interviews


# Topics

## Trees
A tree is an **undirected graph** that satisfies any of the following definitions:
- An acyclic connected graph
- A connected graph with N nodes and N-1 edges
- A graph in which two vertices are connected by exactly one path

![Image of Trees](/images/Trees.png)  
Image Source: https://youtu.be/RBSGKlAvoiM


## Binary Trees and Binary Search Trees (BST)
A **Binary Tree** is a tree where each node has atmost 2 children. 

![Image of Binary Trees](/images/BinaryTree.png)  
Image Source: https://youtu.be/RBSGKlAvoiM

A **Binary Search Tree** is a binary tree that satisfies the **BST invariant**: left subtree has smaller elements and right subtree has larger elements

![Image of Binary Trees](/images/BinarySearchTree.png)  
Image Source: https://youtu.be/RBSGKlAvoiM

### Complexity of Binary Search Trees

| Operation 	| Average   	| Worst 	|
|-----------	|-----------	|-------	|
| Insert    	| O(log(n)) 	| O(n)  	|
| Delete    	| O(log(n)) 	| O(n)  	|
| Remove    	| O(log(n)) 	| O(n)  	|
| Search    	| O(log(n)) 	| O(n)  	|

Depending on the data, you might end up with a linear tree and this is **very bad** since the complexity for all operations on this tree is O(n). This is the worst case described above. For example, see below:

![Image of Binary Trees](/images/LinearBST.png)  
Image Source: https://youtu.be/RBSGKlAvoiM

### BST Operations
#### Insert
When inserting a new value at node position, there are three possible cases:  
   - New value is > value in current node position. In this case, recurse down right sub-tree
   - New value is < value in current node position. In this case, recurse down left sub-tree
   - New value = value in current node position. Here you will need to decide to either insert left or right if your BST supports duplicates; otherwise just ignore new value insert.
   - No node exists at node position. In this case, create new node with new value.  

## Heaps
A heap is a tree based data structure that satisfies the heap invariant (a.k.a heap property): If A is the parent node of B, then A is ordered with respect to B for all nodes A, B in the heap.
 - If A is <=B, this will result in a **Min Heap**
 - If A is >=B, this will result in a **Max Heap**

![Image of Heaps](/images/Heaps.png)   
Image Source: https://youtu.be/RBSGKlAvoiM


## Priority Queues
A priority queue is an abstract data type (ADT) that operations similar to a normal queue except that each element has a certain priority. The priority of the elements in a PQ determine the order in which they are removed. 

**Note**: Priority Queues only support comparable data, meaning the data inserted into a priority queue must be able to be ordered in some way, either in ascending or descending order.

Priority Queues are often implemented via min heaps or max heaps. 

