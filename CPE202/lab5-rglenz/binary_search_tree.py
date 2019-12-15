from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root is None:
            return True
        return False 

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        elif self.root.key == key:
            return True    
        return self.search_helper(key,self.root)
            
    def search_helper(self, key, current):
        if current is not None:
            if key == current.key:
                return True
            elif key > current.key:
                return self.search_helper(key,current.right)
            elif key < current.key:
                return self.search_helper(key,current.left)    
        return False
        

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        node=TreeNode(key,data)
        if self.is_empty():
            self.root=node
        current=self.root
        while True:
            if node.key == current.key:
                current.data=node.data
                break
            if node.key>current.key and current.right is not None:
                current=current.right
            elif node.key<current.key and current.left is not None:
                current=current.left
            else:
                if node.key>current.key:
                    current.right=node
                elif node.key<current.key:
                    current.left=node
                break         

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None 
        node=self.root
        while node.left != None:
            node=node.left
        return node.key,node.data

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.root is None:
            return None 
        node=self.root
        while node.right != None:
            node=node.right
        return node.key,node.data

    def tree_height(self): # return the height of the tree
	        # returns None if tree is empty
        if self.is_empty():
            return None
        if self.root.left is None and self.root.right==None:
            return 0
        else:
            return self.tree_height_helper(self.root)
	
    def tree_height_helper(self,node):
	        left=right=0
	        if node.left is not None:
	            left=self.tree_height_helper(node.left)+1
	        if node.right is not None:
	            right=self.tree_height_helper(node.right)+1
	        if left>right:
	            return left
	        else:
	            return right

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        lst=[]
        return(self.inorder_list_helper(self.root,lst))

    def inorder_list_helper(self, node, lst):
        if node is not None:
            self.inorder_list_helper(node.left,lst)
            lst.append(node.key)
            self.inorder_list_helper(node.right,lst)
        return lst
        
    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        lst=[]
        return(self.preorder_list_helper(self.root,lst))

    def preorder_list_helper(self, node, lst):
        if node is not None:
            lst.append(node.key)
            self.preorder_list_helper(node.left,lst)
            self.preorder_list_helper(node.right,lst)
        return lst
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        q.enqueue(self.root)
        lst=[]
        if self.root is None:
            return []
        if self.root.left is None and self.root.right is None:
            lst.append(self.root.key)
            return lst
        while q.is_empty()==False:
            node=q.dequeue()
            lst.append(node.key)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)
        return lst
        

