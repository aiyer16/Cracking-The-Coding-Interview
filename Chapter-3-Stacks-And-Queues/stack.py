class Stack:
    top = None
    length = 0

    class StackNode:
        data = None
        next = None

        def __init__(self, data):
            self.data = data

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
        return (self.top == None)


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
