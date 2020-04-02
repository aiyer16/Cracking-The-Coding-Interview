import unittest

from . import stack as st


class TestStack(unittest.TestCase):
    def setUp(self):
        self.my_stack = st.Stack()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(4)

    def test_push_items(self):
        self.assertEqual(3, self.my_stack.length)

    def test_pop_item(self):
        item = self.my_stack.pop()
        self.assertEqual(4, item)

    def test_is_empty(self):
        my_stack = st.Stack()
        self.assertTrue(my_stack.is_empty())

    def test_peek_stack(self):
        self.assertEqual(4, self.my_stack.peek())

    def test_peek_empty_stack(self):
        my_stack = st.Stack()
        self.assertRaises(IndexError, my_stack.peek)

    def test_min_stack(self):
        my_stack = st.MinStack()
        my_stack.push(2)
        my_stack.push(2)
        my_stack.push(3)
        my_stack.push(4)
        my_stack.push(1)
        my_stack.push(-1)

        min = my_stack.min()

        self.assertEqual(-1, min)


if __name__ == "__main__":
    unittest.main()
