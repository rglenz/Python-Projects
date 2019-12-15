import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
         
    def test_eq(self):
        loc1 = Location('SLO',35.3,-120.7)
        loc2 = Location('SLO',35.3,-120.7)
        loc3 = Location('SLO',35.1,-120.7)
        loc4 = Location('hi',35.3,-120.7)
        loc5 = Location('SLO',35.3,120)
        self.assertTrue(loc1==loc2)
        self.assertFalse(loc1==loc3)
        self.assertFalse(loc1==loc4)
        self.assertFalse(loc1==loc5)
if __name__ == "__main__":
        unittest.main()
