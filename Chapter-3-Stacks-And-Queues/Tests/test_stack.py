import unittest
import sys
import io

from .. import stack as st

class TestStack(unittest.TestCase):
    def test_push_item(self):
        my_stack = st.Stack()
        my_stack.push(1)
        my_stack_length = my_stack.length

        self.assertEqual(1, my_stack_length)

if __name__ == "__main__":
    unittest.main()

