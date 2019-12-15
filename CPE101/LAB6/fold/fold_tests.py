#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9
import unittest
import fold 

class TestCases(unittest.TestCase):
   def test_sum(self):
      self.assertEqual(fold.sum([[1,2,3],[1,2]]),9)
      self.assertEqual(fold.sum([1,2,3,4,5,6,7]),28)
      self.assertEqual(fold.sum([1,21,30]),52)
      pass

   def test_index_of_smallest(self):
      self.assertEqual(fold.index_of_smallest([4,[-1,2]]),1)
      self.assertEqual(fold.index_of_smallest([10,5,3,4,5,6,7]),2)
      self.assertEqual(fold.index_of_smallest([]),-1)
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

