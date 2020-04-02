import unittest

from . import queue as q


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.my_queue = q.Queue()
        self.my_queue.add(1)
        self.my_queue.add(3)
        self.my_queue.add(4)

    def test_add_item(self):
        self.assertEqual(3, self.my_queue.length)

    def test_remove_item(self):
        item = self.my_queue.remove()
        self.assertEqual(1, item)

    def test_peek_queue(self):
        item = self.my_queue.peek()
        self.assertEqual(1, item)

    def test_peek_empty_queue(self):
        my_queue = q.Queue()
        self.assertRaises(IndexError, my_queue.peek)

if __name__ == '__main__':
    unittest.main()
