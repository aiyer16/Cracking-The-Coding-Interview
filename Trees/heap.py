class MinHeap:

    def __init__(self, node=None):
        """Constructor"""
        self.size = 0
        self.heap = []

        if node is not None:
            self.heap.append(node)
            self.size += 1

    def parent(self, pos):
        """Returns position of parent given position of any element"""
        # In a zero-indexed array, parent of any element at i is floor((i-1)/2)
        return (pos - 1)//2

    def left_child(self, pos):
        """Returns position of left child given position of any element"""
        # In a zero-indexed array, left child of any element at i is 2*i+1
        return 2*pos + 1

    def right_child(self, pos):
        """Returns position of right child given position of any element"""
        # In a zero-indexed array, left child of any element at i is 2*i+2
        return 2*pos + 2

    def min(self):
        """Returns min element of heap (this is the root)"""
        return self.heap[0]

    def swap(self, pos_1, pos_2):
        """Swaps two nodes in heap given their positions"""
        self.heap[pos_1], self.heap[pos_2] = self.heap[pos_2], self.heap[pos_1]

    def is_leaf_node(self, pos):
        """Returns true if given position is in the leaf of tree,
        else returns false
        """
        # In a zero-indexed array, elements n/2 to n are leaf nodes
        if pos >= (self.size//2) and pos < self.size:
            return True
        else:
            return False

    def _heapify(self, pos):
        """
        Bubbles elements down starting at given position to maintain
        min heap constraints
        """
        # Only do anything for non-leaf node positions
        if not self.is_leaf(pos):
            # If parent is greater than either child, it needs
            # to be bubbled down
            if (self.heap[pos] > self.heap[self.left_child(pos)] or
                    self.heap[pos] > self.heap[self.right_child(pos)]):

                # If the left child is less that or equal to right
                # swap parent with left child and recurse
                # else swap parent with right child and recurse
                if (self.heap[self.left_child(pos)]
                        <= self.heap[self.right_child(pos)]):
                    self.swap(pos, self.left_child(pos))
                    self._heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self._heapify(self.right_child(pos))

    def insert(self, node):
        """Inserts a new node to heap"""
        # First insert node at the end
        current_pos = self.size
        self.heap.append(node)
        self.size += 1

        # Bubble up newly inserted node until
        # it is less that it's parent
        while (self.heap[current_pos] > self.heap[self.parent(current_pos)]):
            swap(current_pos, self.parent(current_pos))
            current_pos = self.parent(current_pos)

    def print(self):
        """Prints the heap"""
        for i in range(0, (self.size/2)):
            print(f"PARENT: {self.heap[i]}; \
                    LEFT CHILD: {self.heap[self.left_child(i)]} \
                    RIGHT CHILD: {self.heap[self.right_child(i)]}")


class MaxHeap:
    pass
