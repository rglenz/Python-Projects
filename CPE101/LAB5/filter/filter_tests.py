import unittest
import filter

class TestCases(unittest.TestCase):
   def test_are_positiveTest(self):
      self.assertEqual(filter.are_positive([1,2,3]),[2])
      self.assertEqual(filter.are_positive([6,2,3]),[6,2])
      self.assertEqual(filter.are_positive([1,2,3,8,10]),[2,8,10])
   def test_are_greater_than_nTest(self):
      self.assertEqual(filter.are_positive([1,2,3]),[2])
      self.assertEqual(filter.are_positive([6,2,3]),[6,2])
      self.assertEqual(filter.are_positive([1,2,3,8,10]),[2,8,10])   
   def test_are_divisible_by_n(self):
      self.assertEqual(filter.are_divisible_by_n([1,2,3],2),[2])
      self.assertEqual(filter.are_divisible_by_n([6,2,3],3),[6,3])
      self.assertEqual(filter.are_divisible_by_n([1,2,3,8,10],2),[2,8,10])   
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

