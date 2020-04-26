import unittest

from . import heap


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        self.my_heap = heap.MinHeap(15)

    def test_min(self):
        self.assertEqual(15, self.my_heap.min())

    # def test_insert_item(self):
    #     self.my_heap.insert(15)
    #     self.my_heap.insert(5)
    #     self.my_heap.insert(3)
    #     self.my_heap.insert(17)
    #     self.my_heap.insert(10)
    #     self.my_heap.insert(84)
    #     self.my_heap.insert(19)
    #     self.my_heap.insert(6)
    #     self.my_heap.insert(22)
    #     self.my_heap.insert(9)


if __name__ == "__main__":
    unittest.main()
