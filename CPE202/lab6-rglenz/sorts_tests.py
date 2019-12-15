import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    def test_simple_ins(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])
    def test_01_sel(self):
        nums = [23,10,15,34,45,6,7]
        comps=selection_sort(nums)
        self.assertEqual(comps, 21)
        self.assertEqual(nums, [6,7,10,15,23,34,45])
    def test_01_ins(self):
        nums = [23,10,15,34,45,6,7]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 16)
        self.assertEqual(nums, [6,7,10,15,23,34,45])
    def test_02_ins(self):
        nums = [18,12,16,3,14]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 9)
        self.assertEqual(nums, [3,12,14,16,18])
    def test_sorted_ins(self):
        nums = [1,2,3,4,5,6]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 5)
        self.assertEqual(nums, [1,2,3,4,5,6])
    def test_sorted_sel(self):
        nums = [1,2,3,4,5,6]
        comps = selection_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [1,2,3,4,5,6])
    def test_sorted_ins_01(self):
        nums = [50,40,30,20,10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [10,20,30,40,50])
    def test_sorted_sel_03(self):
        nums = [50,40,30,20,10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 10)
        self.assertEqual(nums, [10,20,30,40,50])



if __name__ == '__main__': 
    unittest.main()
