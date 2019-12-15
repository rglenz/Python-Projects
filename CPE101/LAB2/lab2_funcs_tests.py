#Lab 2 Test Cases
#Name:Raymond Lenz
#Section:9
##############################################################
import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_math_func1(self):
      self.assertAlmostEqual(funcs.math_func1(1,2),.75)
      self.assertAlmostEqual(funcs.math_func1(2,3),2.0588235294117645)
      pass


   def test_math_func2(self):
      self.assertAlmostEqual(funcs.math_func2(1,2,1),-1)
      self.assertAlmostEqual(funcs.math_func2(1,-2,1),1)
      pass

   def test_math_func3(self):
      self.assertAlmostEqual(funcs.math_func3(3,-1,5,2),5)
      self.assertAlmostEqual(funcs.math_func3(4,1,5,1),5)
      pass
      
   def test_is_negative(self):
      self.assertTrue(funcs.is_negative(-1))
      self.assertFalse(funcs.is_negative(1))
      pass

   def test_dividable_by_5(self):
      self.assertTrue(funcs.is_dividable_by_5(10))
      self.assertFalse(funcs.is_dividable_by_5(3))
      pass

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

