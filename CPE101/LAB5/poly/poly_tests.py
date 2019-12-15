import unittest
import poly

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_poly_add2(self):
      self.assertListAlmostEqual(poly.poly_add2([2.3,4.7,1.0],[1.2,2.1,-3.2]),[3.5,6.8,-2.2])
      self.assertListAlmostEqual(poly.poly_add2([1,2,3],[3,2,1]),[4,4,4])
      self.assertListAlmostEqual(poly.poly_add2([1,2,5],[6,8,2]),[7,10,7])
   
   def test_poly_mult2(self):
      self.assertListAlmostEqual(poly.poly_mult2([3,2],[2,2]),[6,10,4])
      self.assertListAlmostEqual(poly.poly_mult2([3,2],[-1,1]),[-3,1,2])
      self.assertListAlmostEqual(poly.poly_mult2([2,2],[-1,1]),[-2,0,2])
if __name__ == '__main__':
   unittest.main()
