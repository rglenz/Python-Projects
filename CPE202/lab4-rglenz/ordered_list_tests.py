import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        t_list.add(20)
        self.assertEqual(t_list.pop(0), 10)
    def test_1(self):
        t_list = OrderedList()
        t_list.add(50)
        t_list.add(30)
        t_list.add(20)
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10,20,30,50])
        self.assertEqual(t_list.python_list_reversed(),[50,30,20,10])
        self.assertEqual(t_list.index(30), 2)
    def test_2(self):
        t_list = OrderedList()
        t_list.add(-50)
        t_list.add(30.40)
        t_list.add(30.39)
        self.assertEqual(t_list.python_list(), [-50,30.39,30.40])
        self.assertEqual(t_list.python_list_reversed(),[30.4,30.39,-50])
        self.assertEqual(t_list.index(30.39), 1)
        self.assertEqual(t_list.index(568), None)
        self.assertFalse(t_list.search(10))
        self.assertTrue(t_list.search(-50))
        self.assertTrue(t_list.remove(30.39))
        self.assertFalse(t_list.remove(7890))
        self.assertEqual(t_list.python_list(), [-50,30.40])
        self.assertEqual(t_list.python_list_reversed(),[30.4,-50])
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.pop(1), 30.40)
        self.assertEqual(t_list.pop(0), -50)
        self.assertTrue(t_list.is_empty())
    def test_Errors(self):
        t_list = OrderedList()
        t_list.add(40)
        t_list.add(2)
        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(-2)
        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(2)
        with self.assertRaises(IndexError):  # used to check for exception
            t_list.pop(3)
        
        
       
   

if __name__ == '__main__': 
    unittest.main()
