import unittest
import map

class TestCases(unittest.TestCase):
   def test_square_all(self):
      self.assertEqual(map.square_all([1,2,3]),[1,4,9])
      self.assertEqual(map.square_all([4,5,6,4]),[16,25,36,16])
      self.assertEqual(map.square_all([1,4,5]),[1,16,25])
      pass
   
   def test_add_n_all(self):
      self.assertEqual(map.add_n_all([1,2,3],4),[5,6,7])
      self.assertEqual(map.add_n_all([5,6,10],10),[15,16,20])
      self.assertEqual(map.add_n_all([4,4,7],5),[9,9,12])
      pass
   def test_even_or_odd_all(self):
      self.assertEqual(map.even_or_odd_all([1,2,3]),[False,True,False])
      self.assertEqual(map.even_or_odd_all([16,45,46]),[True,False,True])
      self.assertEqual(map.even_or_odd_all([1,3,7,9]),[False,False,False,False])
      pass
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

