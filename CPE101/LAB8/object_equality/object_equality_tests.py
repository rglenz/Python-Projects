#Raymond Lenz
#Sussan Einakian
#Section 9
#Lab 8
import unittest
import objects as o

class TestCases(unittest.TestCase):
   def test_equality(self):
      p=o.Point(2,3)
      p1=o.Point(2,3)
      self.assertTrue(p1==p)
      p3=o.Point(4,5)
      p4=o.Point(4,5)
      self.assertFalse(p1==p3)
      self.assertTrue(p3==p4)
      pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

