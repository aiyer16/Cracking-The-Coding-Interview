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
