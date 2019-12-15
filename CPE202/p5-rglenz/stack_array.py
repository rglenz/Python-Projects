class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        '''Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance'''
        if self.num_items != 0:
            return False
        return True

    def is_full(self):
        '''Returns True if the stack is full, and False otherwise
           MUST have O(1) performance'''
        if self.num_items==self.capacity:
            return True 
        return False

    def push(self, item):
        '''If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_full():
            raise IndexError
        else:
            length=self.size()
            self.items[length]=item
        self.num_items+=1


    def pop(self): 
        '''If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            item=self.items[self.size()-1]
            self.items[self.size()-1]=None
            self.num_items-=1
            return item

    def peek(self):
        '''If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance'''
        if self.is_empty():
            raise IndexError
        else:
            return(self.items[self.size()-1])

    def size(self):
        '''Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance'''
        return(self.num_items)

 