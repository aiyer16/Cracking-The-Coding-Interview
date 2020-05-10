import unittest
import io
import sys

from . import heap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.my_heap = heap.MinHeap(15)

    def test_min(self):
        self.assertEqual(15, self.my_heap.min())

    def test_parent(self):
        self.assertEqual(2, self.my_heap.parent(5))

    def test_parent_root(self):
        self.assertEqual(0, self.my_heap.parent(0))

    def test_left_child(self):
        self.assertEqual(3, self.my_heap.left_child(1))

    def test_left_child_root(self):
        self.assertEqual(1, self.my_heap.left_child(0))

    def test_right_child(self):
        self.assertEqual(4, self.my_heap.right_child(1))

    def test_right_child_root(self):
        self.assertEqual(2, self.my_heap.right_child(0))

    def test_swap(self):
        my_heap = heap.MinHeap([5, 15, 1])
        my_heap.swap(1, 2)

        self.assertListEqual([5, 1, 15], my_heap.heap)

    def test_heapify(self):
        my_heap = heap.MinHeap([5, 15, 1, 2])
        my_heap.heapify()

        self.assertListEqual([1, 2, 5, 15], my_heap.heap)

    def test_insert_check_min(self):
        self.my_heap.insert(5)
        self.my_heap.insert(3)
        self.my_heap.insert(17)
        self.my_heap.insert(10)
        self.my_heap.insert(84)
        self.my_heap.insert(19)
        self.my_heap.insert(6)
        self.my_heap.insert(22)
        self.my_heap.insert(9)

        self.assertEqual(3, self.my_heap.min())

    def test_insert_check_heap(self):
        self.my_heap.insert(5)
        self.my_heap.insert(3)
        self.my_heap.insert(17)
        self.my_heap.insert(10)

        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput     # and redirect stdout.
        self.my_heap.print()
        sys.stdout = sys.__stdout__     # Reset redirect.

        self.assertEqual(
            "PARENT: 3; LEFT CHILD: 10; RIGHT CHILD: 5" + "\n" +
            "PARENT: 10; LEFT CHILD: 17; RIGHT CHILD: 15" + "\n",
            capturedOutput.getvalue())


if __name__ == "__main__":
    unittest.main()
