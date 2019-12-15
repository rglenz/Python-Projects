#Raymond Lenz
#Sussan Einakian 
#Section 9 
#Lab 8
import unittest
import list_comp as l
import objects as o

class TestCases(unittest.TestCase):
   def test_1(self):
      self.assertAlmostEqual(l.distance_all([o.Point(1,2),o.Point(3,2),o.Point(4,3),o.Point(0,0)]),[2.23606797749979, 3.605551275463989,5.0,0.0])
      self.assertAlmostEqual(l.distance_all([o.Point(1,0),o.Point(2,0),o.Point(4,3),o.Point(0,0)]),[1,2,5,0])
      self.assertAlmostEqual(l.distance_all([o.Point(3,0),o.Point(0,6),o.Point(4,3),o.Point(0,0)]),[3,6,5,0])
      pass
   def test_2(self):
      self.assertEqual(l.are_in_first_quadrant([o.Point(1,2),o.Point(-1,2)]),[o.Point(1,2)])
      self.assertEqual(l.are_in_first_quadrant([o.Point(-1,2),o.Point(-1,2),o.Point(3,2),o.Point(1,4)]),[o.Point(3,2),o.Point(1,4)])
      self.assertEqual(l.are_in_first_quadrant([o.Point(-1,2),o.Point(-1,2)]),[])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

