import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #Checks max list if the list is empty 
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    def test_max_list_iter_same_max(self):
        #this checks that the max function will still run even if the max is repeated
        tlist=[1,2,3,0,3]
        self.assertEqual(max_list_iter(tlist), 3 )
    def test_max_list_iter_repeated_max(self):
        #checks if it will still run even if max is right next to an equal max
        tlist=[1,2,3,3]
        self.assertEqual(max_list_iter(tlist), 3 )
    def test_max_list_iter_repeated_max(self):
        #checks to see if the function will run with negative numbers 
        tlist=[-11,-2,3]
        self.assertEqual(max_list_iter(tlist), 3 )
        tlist=[-11,-2,-3]
        self.assertEqual(max_list_iter(tlist), -2 )
    def test_max_list_iter_repeated_max(self):
        #checks to see if the function will run with floats 
        tlist=[.1,.2,.3]
        self.assertEqual(max_list_iter(tlist), .3 )
        tlist=[-1.1,-.2,-.3]
        self.assertEqual(max_list_iter(tlist), -.2 )

    def test_reverse_rec_empty(self):
        #checks is it will catch the empty list 
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
    def test_reverse_rec_(self):
        #checks if it will still reverse correctly with floats and negative numbers
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1.1,30.5,5]),[5,30.5,1.1])
        self.assertEqual(reverse_rec([-1,-2,-3]),[-3,-2,-1])
        self.assertEqual(reverse_rec([-1.1,-30.5,-5]),[-5,-30.5,-1.1])
        
    def test_bin_search(self):
        #Test all values from 0-10
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(0, low, high, list_val), 0 )
        self.assertEqual(bin_search(1, low, high, list_val), 1 )
        self.assertEqual(bin_search(2, low, high, list_val), 2 )
        self.assertEqual(bin_search(3, low, high, list_val), 3 )
        self.assertEqual(bin_search(4, low, high, list_val), 4 )
        #test values that do not exist 
        self.assertEqual(bin_search(5, low, high, list_val), None )
        self.assertEqual(bin_search(6, low, high, list_val), None )
        self.assertEqual(bin_search(7, low, high, list_val), 5 )
        self.assertEqual(bin_search(8, low, high, list_val), 6 )
        self.assertEqual(bin_search(9, low, high, list_val), 7)
        self.assertEqual(bin_search(10, low, high, list_val), 8)
        
    def test_bin_search_high_is_lower(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 9, 0, list_val), None )
        self.assertEqual(bin_search(4, 1, 0, list_val), None )
    def test_bin_search_empty(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(0,0,10,tlist)
if __name__ == "__main__":
        unittest.main()

    

    
