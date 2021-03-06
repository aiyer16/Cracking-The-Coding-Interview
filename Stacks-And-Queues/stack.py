class Stack:

    def __init__(self):
        self.top = None
        self.length = 0

    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def pop(self):
        """Retrieve last item from stack"""
        if self.top is None:
            raise IndexError

        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item

    def push(self, data):
        """Add new item to stack"""
        new_top = self.StackNode(data)
        new_top.next = self.top
        self.top = new_top
        self.length += 1

    def peek(self):
        """Return value of last item in stack"""
        if self.top is None:
            raise IndexError

        return self.top.data

    def is_empty(self):
        """Returns True if stack is empty"""
        return (self.top is None)


class MinStack(Stack):
    # Create a new stack to store all min values
    min_values = Stack()

    def push(self, data):
        """Add new item to stack"""
        # Call the push method of the super class first
        super(MinStack, self).push(data)

        # If top of current stack is less than top of min_values stack
        # Store the new min value in the min_values stack
        # If min_values_stack is empty, store top of current stack as min
        try:
            if (self.top.data < self.min_values.peek()):
                self.min_values.push(self.top.data)
        except IndexError:
            self.min_values.push(self.top.data)

    def pop(self):
        """Retrieve last item from stack"""
        # Call the pop method of the super class first
        item = super(MinStack, self).pop()

        # If value popped from current stack equals top of min_values stack
        # Pop the top of the min_values stack as well
        try:
            if (item == self.min_values.peek()):
                self.min_values.pop()
        except IndexError:
            return None

    def min(self):
        """Return min value of stack"""
        return self.min_values.peek()


def sort(unsorted_stack: Stack, order='desc') -> Stack:
    """Sort stack based in ascending or descending order"""
    if (unsorted_stack.is_empty()):
        return unsorted_stack

    if order.lower() == 'desc':
        def sort_inner_asc(unsorted_stack: Stack,
                           sorted_stack: Stack, temp_stack: Stack):
            if (sorted_stack.is_empty()):
                sorted_stack.push(unsorted_stack.pop())
            elif (sorted_stack.peek() <= unsorted_stack.peek()):
                sorted_stack.push(unsorted_stack.pop())
            else:
                temp_stack.push(sorted_stack.pop())
                sort_inner_asc(unsorted_stack, sorted_stack, temp_stack)

            while not (temp_stack.is_empty()):
                sorted_stack.push(temp_stack.pop())

            return

        temp_stack = Stack()
        sorted_stack = Stack()

        while not(unsorted_stack.is_empty()):
            sort_inner_asc(unsorted_stack, sorted_stack, temp_stack)

        return sorted_stack
    elif order.lower() == 'asc':
        sorted_stack = Stack()

        while not(unsorted_stack.is_empty()):
            # Insert each element in unsorted_stack
            # in sorted order into sorted_stack
            temp = unsorted_stack.pop()

            while (not sorted_stack.is_empty() and sorted_stack.peek() < temp):
                unsorted_stack.push(sorted_stack.pop())

            sorted_stack.push(temp)

        return sorted_stack
    else:
        raise ValueError('Order must be either ascending or descending')
