import unittest
#from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()
    def test_simple(self):
        q = Queue(5)
        q.enqueue(1)
        self.assertEqual(q.dequeue(),1)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),0)
    def test_1(self):
        q = Queue(5)
        q.enqueue(0)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.enqueue(9)
        self.assertEqual(q.dequeue(),0)
        self.assertEqual(q.dequeue(),3)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),3)
    def test_2(self):
        q = Queue(3)
        q.enqueue(20)
        q.enqueue(-3)
        q.enqueue(5647)
        self.assertEqual(q.dequeue(),20)
        self.assertEqual(q.dequeue(),-3)
        self.assertEqual(q.dequeue(),5647)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),0)
        q.enqueue(20)
        q.enqueue(-3)
        q.enqueue(5647)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(),3)
    def test_3(self):
        q = Queue(3)
        q.enqueue(7.4)
        q.enqueue(3.2)
        q.enqueue(8.9)
        self.assertEqual(q.dequeue(),7.4)
        self.assertEqual(q.dequeue(),3.2)
        self.assertEqual(q.dequeue(),8.9)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(),0)
        q.enqueue(7.4)
        q.enqueue(3.2)
        q.enqueue(8.9)
        self.assertEqual(q.dequeue(),7.4)
        q.enqueue(8.9)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertEqual(q.size(),3)
    
    def test_Errors(self):
        q = Queue(1)
        with self.assertRaises(IndexError):  # used to check for exception
            q.dequeue()
        q.enqueue(1)
        with self.assertRaises(IndexError):  # used to check for exception
            q.enqueue(2)
   
    

    
if __name__ == '__main__': 
    unittest.main()
