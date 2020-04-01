class Stack:
    top = None
    length = 0

    class StackNode:
        data = None
        next = None

        def __init__(self, data):
            self.data = data

    def pop(self):
        """Method to retrieve last item from stack"""
        if self.top is None:
            raise IndexError

        item = self.top.data
        self.top = self.top.next
        self.length -= 1
        return item
    
    def push(self, data):
        """Method to add new item to stack"""
        new_top = self.StackNode(data)
        new_top.next = self.top
        self.top = new_top
        self.length += 1

    def peek(self):
        """Method to return value of last item in stack"""
        if self.top is None:
            raise IndexError
        
        return self.top.data
    
    def is_empty(self):
        return (self.top == None)
