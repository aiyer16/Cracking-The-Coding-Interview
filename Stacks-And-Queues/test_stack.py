import unittest

from . import stack as st


class TestStack(unittest.TestCase):
    def setUp(self):
        self.my_stack = st.Stack()
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.my_stack.push(4)
        self.my_stack.push(3)
        self.my_stack.push(6)

    def test_push_items(self):
        self.assertEqual(5, self.my_stack.length)

    def test_pop_one_item(self):
        item = self.my_stack.pop()
        self.assertEqual(6, item)

    def test_is_empty(self):
        my_stack = st.Stack()
        self.assertTrue(my_stack.is_empty())

    def test_peek_stack(self):
        self.assertEqual(6, self.my_stack.peek())

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

    def test_sort_desc(self):
        sorted_stack = st.sort(self.my_stack, order='desc')
        output_list_expected = [6, 4, 3, 2, 1]
        output_list = []

        while not (sorted_stack.is_empty()):
            output_list.append(sorted_stack.pop())

        self.assertEqual(output_list_expected, output_list)

    def test_sort_asc(self):
        sorted_stack = st.sort(self.my_stack, order='asc')
        output_list_expected = [1, 2, 3, 4, 6]
        output_list = []

        while not (sorted_stack.is_empty()):
            output_list.append(sorted_stack.pop())

        self.assertEqual(output_list_expected, output_list)


if __name__ == "__main__":
    unittest.main()
