class Queue:
    first = None
    last = None
    length = 0

    class QueueNode:
        data = None
        next = None

        def __init__(self, data):
            self.data = data

    def add(self, data):
        """Add an item to the end of queue"""
        new_last = self.QueueNode(data)

        if (self.last is not None):
            self.last.next = new_last

        self.last = new_last

        if (self.first is None):
            self.first = self.last

        self.length += 1

    def remove(self):
        """Remove the first item in the queue"""
        if (self.first is None):
            raise IndexError

        item = self.first.data
        self.first = self.first.next

        if (self.first is None):
            self.last == None

        self.length -= 1

        return item

    def peek(self):
        """Return the top of the queue"""
        if (self.first is None):
            raise IndexError

        return self.first.data

    def is_empty(self):
        return self.first == None
