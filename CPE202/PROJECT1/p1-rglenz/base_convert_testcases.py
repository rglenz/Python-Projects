import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(0,2),"0")
        self.assertEqual(convert(1,2),"1")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(1,4),"1")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
    
    def test_base3(self):
        self.assertEqual(convert(127,3),"11201")

    def test_base5(self):
        self.assertEqual(convert(56,5),"211")

    def test_base6(self):
        self.assertEqual(convert(378,6),"1430")
    
    def test_base7(self):
        self.assertEqual(convert(66,7),"123")

    def test_base8(self):
        self.assertEqual(convert(657,8),"1221")

    def test_base9(self):
        self.assertEqual(convert(457,9),"557")

    def test_base10(self):
        self.assertEqual(convert(127,10),"127")

    def test_base11(self):
        self.assertEqual(convert(1000,11),"82A")

    def test_base12(self):
        self.assertEqual(convert(567,12),"3B3")
    
    def test_base13(self):
        self.assertEqual(convert(420,13),"264")

    def test_base14(self):
        self.assertEqual(convert(1200,14),"61A")

    def test_base15(self):
        self.assertEqual(convert(136,15),"91")

    def test_base16(self):
        self.assertEqual(convert(457,16),"1C9")
        self.assertEqual(convert(1,16),"1")
        self.assertEqual(convert(11259375,16),"ABCDEF")

if __name__ == "__main__":
        unittest.main()