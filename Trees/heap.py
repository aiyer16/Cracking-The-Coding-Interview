class MinHeap:

    def __init__(self, node=None):
        """Constructor"""
        self.size = 0
        self.heap = []

        if node is not None:
            if isinstance(node, list):
                self.heap = node
                self.size = len(node)
            else:
                self.heap.append(node)
                self.size += 1

    def parent(self, pos):
        """Returns position of parent given position of any element"""
        # In a zero-indexed array, parent of any element at i is floor((i-1)/2)
        return (pos - 1)//2 if pos > 0 else 0

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

    def _heapify_node(self, pos):
        """
        Heapifies node at given position
        """
        # Only do anything for non-leaf node positions
        if not self.is_leaf_node(pos):
            # If parent is greater than either child, it needs
            # to be bubbled down
            left_pos = self.left_child(pos)
            right_pos = self.right_child(pos)

            left_child = self.heap[left_pos]

            right_child = self.heap[right_pos] if (
                right_pos > 0 and right_pos < self.size) else None

            if (self.heap[pos] > left_child or
                    self.heap[pos] > right_child):

                # If the left child is less than or equal to right
                # swap parent with left child and recurse
                # else swap parent with right child and recurse
                if right_child is None or (left_child
                                           <= right_child):
                    self.swap(pos, left_pos)
                    self._heapify_node(left_pos)
                else:
                    self.swap(pos, right_pos)
                    self._heapify_node(right_pos)

    def heapify(self):
        """
        Heapifies the current heap
        """
        for pos in range((self.size//2)-1, -1, -1):
            self._heapify_node(pos)

    def insert(self, node):
        """Inserts a new node to heap"""
        # First insert node at the end
        current_pos = self.size
        self.heap.append(node)
        self.size += 1

        # Bubble up newly inserted node until
        # it is less that it's parent
        while (self.heap[current_pos] < self.heap[self.parent(current_pos)]):
            self.swap(current_pos, self.parent(current_pos))
            current_pos = self.parent(current_pos)

    def print(self):
        """Prints the heap"""
        for i in range(0, (self.size//2)):
            print(
                f"PARENT: {self.heap[i]}; " +
                f"LEFT CHILD: {self.heap[self.left_child(i)]}; " +
                f"RIGHT CHILD: {self.heap[self.right_child(i)]}")

    def extract_min(self):
        """Returns min node and removes it from heap"""
        pass


class MaxHeap:
    pass
