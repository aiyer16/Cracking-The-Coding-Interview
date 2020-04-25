# Cracking-The-Coding-Interview

This repository contains code for common data structures and algorthms in Python to help with cracking the coding interview, specifically for the Data Engineer role. The topics discussed here have been collected from various sources including Cracking the Coding Interview (6th Edition) by Gayle Laakmann McDowell. The motivation behind this project is to:

- Improving my own skills on key topics of data structures and algorithms
- Provide a reference to others preparing for interviews

# Topics

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
