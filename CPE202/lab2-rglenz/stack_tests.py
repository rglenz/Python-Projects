import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertEqual(stack.pop(),0)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)
    def test_1(self):
        stack = Stack(5)
        stack.push(0)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        stack.push(9)
        self.assertEqual(stack.pop(),9)
        self.assertEqual(stack.pop(),5)
        self.assertEqual(stack.peek(),4)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),3)
    def test_2(self):
        stack = Stack(3)
        stack.push(20)
        stack.push(-3)
        stack.push(5647)
        self.assertEqual(stack.pop(),5647)
        self.assertEqual(stack.pop(),-3)
        self.assertEqual(stack.peek(),20)
        self.assertEqual(stack.pop(),20)
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),0)
        stack.push(20)
        stack.push(-3)
        stack.push(5647)
        self.assertEqual(stack.peek(),5647)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),3)
    def test_Errors(self):
        stack = Stack(1)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.pop()
        with self.assertRaises(IndexError):  # used to check for exception
            stack.peek()
        stack.push(1)
        with self.assertRaises(IndexError):  # used to check for exception
            stack.push(2)
if __name__ == '__main__': 
    unittest.main()
