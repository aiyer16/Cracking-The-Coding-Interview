from . import stack as st


class QueueViaStacks:
    
    def __init__(self):
        self.stack_new = st.Stack()
        self.stack_old = st.Stack()

    def add(self, data):
        """Add an item to the end of queue"""
        self.stack_new.push(data)

    def remove(self):
        """Remove the first item in the queue"""
        if (self.stack_new.is_empty()) and (self.stack_old.is_empty()):
            raise IndexError

        if (self.stack_old.is_empty):
            self.refill_old_stack()
            return self.stack_old.pop()
        else:
            return self.stack_old.pop()

    def peek(self):
        """Return the top of the queue"""
        if (self.is_empty()):
            raise IndexError

        if (self.stack_old.is_empty()):
            self.refill_old_stack()
            return self.stack_old.peek()
        else:
            return self.stack_old.peek()

    def is_empty(self):
        """Returns True if queue is empty"""
        return (self.stack_new is None) and (self.stack_old is None)

    def refill_old_stack(self):
        """Transfers contents from new stack to old"""
        while(not self.stack_new.is_empty()):
            item = self.stack_new.pop()
            self.stack_old.push(item)

    def length(self):
        """Returns length of the queue"""
        return (self.stack_new.length + self.stack_old.length)