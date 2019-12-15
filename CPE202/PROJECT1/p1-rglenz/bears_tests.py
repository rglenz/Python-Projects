import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertTrue(bears(84))
    
    def test_bear_05(self):
        self.assertFalse(bears(30))

    def test_bear_06(self):
        self.assertFalse(bears(53))
    #less than 42
    def test_bear_07(self):
        self.assertFalse(bears(41))
    #Test something that doesn't fall under any conditional 
    def test_bear_08(self):
        self.assertFalse(bears(83))

    def test_bear_10(self):
        self.assertFalse(bears(46))
if __name__ == "__main__":
    unittest.main()
