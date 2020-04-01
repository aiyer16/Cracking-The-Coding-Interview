import unittest
import sys
import io

from . import stack as st

class TestStack(unittest.TestCase):
    def test_push_items(self):
        my_stack = st.Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)
        
        my_stack_length = my_stack.length

        self.assertEqual(3, my_stack_length)
    
    def test_pop_item(self):
        my_stack = st.Stack()
        my_stack.push(1)
        my_stack.push(2)
        my_stack.push(3)

        item = my_stack.pop()

        self.assertEqual(3, item)

if __name__ == "__main__":
    unittest.main()

