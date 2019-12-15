class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.dummy=Node(None)
        self.dummy.next=self.dummy
        self.dummy.prev=self.dummy

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.next==self.dummy:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        nitem=Node(item)
        current=self.dummy.next
        while current!= self.dummy and item>current.item:
            current=current.next
        nitem.next=current
        nitem.prev=current.prev
        current.prev.next=nitem
        current.prev=nitem
    

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.search(item)==True:
            idx=self.index(item)
            node=self.dummy.next
            for x in range(0,idx):
                node=node.next
            node.prev.next=node.next
            node.next.prev=node.prev
            return True
        return False

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        node=self.dummy.next
        idx=0
        while node!= self.dummy:
            if node.item==item:
                return idx
            idx+=1
            node=node.next
        return None
        

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index<0:
            raise IndexError
        node=self.dummy.next
        idx=0
        while idx!=index:
            node=node.next
            if node==self.dummy:
                raise IndexError
            idx+=1
        data=node.item
        node.prev.next=node.next
        node.next.prev=node.prev
        return data
        

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.dummy.next,item)
    def search_helper(self,node,item):
        if node.item==item:
            return True
        if node==self.dummy:
            return False
        node=node.next
        return self.search_helper(node,item)
        

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        node=self.dummy.next
        datalst=[]
        while node!= self.dummy:
            datalst.append(node.item)
            node=node.next    
        return datalst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        lst=[]
        return self.list_reverse_helper(self.dummy.prev,lst)
    def list_reverse_helper(self,node,lst): 
        if node is self.dummy:
            return lst
        lst.append(node.item)
        return(self.list_reverse_helper(node.prev,lst))

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.dummy.next)
    
    def size_helper(self,node):
        if node is self.dummy:
            return 0
        return 1+ self.size_helper(node.next)
        