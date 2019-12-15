#Project 6
#Raymond Lenz 
#Sussan Einakian
#Section: 9 
import unittest
import crimetime as c

class TestString(unittest.TestCase):
    def test_binary_search(self):
        self.assertTrue(c.binarySearch([1,2,3,4,5],1))
        self.assertFalse(c.binarySearch([1,2,3,4,5],6))
        self.assertTrue(c.binarySearch([1,2,3,4,5],3))
    def test_create_crimes(self):
        self.assertEqual(c.create_crimes(["1 ROBBERY","2 ROBBERY","3 ROBBERY"]),['1','2','3'])
        self.assertEqual(c.create_crimes(["3 ROBBERY","67 ROBBERY","3 ROBBERY"]),['3','67'])
        self.assertEqual(c.create_crimes(["1 ROBBERY","2 ROBBERY","3 Hey"]),['1','2'])
    def test_sort_crimes(self):
        self.assertEqual(c.sort_crimes(["1 ROBBERY","2 ROBBERY","3 ROBBERY"]),['1 ROBBERY','2 ROBBERY','3 ROBBERY'])
        self.assertEqual(c.sort_crimes(["3 ROBBERY","67 ROBBERY","4 ROBBERY"]),['3 ROBBERY','4 ROBBERY','67 ROBBERY'])
        self.assertEqual(c.sort_crimes(["1 ROBBERY","5 ROBBERY","2 ROBBERY"]),['1 ROBBERY','2 ROBBERY','5 ROBBERY'])
    def test_update_crimes(self):
        self.assertEqual(c.update_crimes(['1'],["1 10/01/2000 01:56"]),[c.Crime('1','ROBBERY','Monday',10,1)])
        self.assertEqual(c.update_crimes(['3'],["3 01/01/2000 02:56"]),[c.Crime('3','ROBBERY','Monday',1,2)])
        self.assertEqual(c.update_crimes(['2'],["4 10/01/2000 01:56"]),[])
        



if __name__=='__main__':
    unittest.main()       
