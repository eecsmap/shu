class Stack:
    '''
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.pop()
    1
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.pop()
    2
    >>> stack.pop()
    1
    '''
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
