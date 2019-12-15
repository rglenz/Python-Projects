import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_quadratic_probe(self):
        ht = HashTable(7)
        ht.insert("catattack", 6)
        ht.insert("catattack1111", 0)
        ht.insert("catattack2222", 1)
        ht.insert("catattack3333", 1)
        self.assertEqual(ht.quadratic_probe("catattack"), 11)
        self.assertEqual(ht.quadratic_probe("catattack1111"), 12)
        self.assertEqual(ht.quadratic_probe("catattack2222"), 0)
        self.assertEqual(ht.quadratic_probe("catattack3333"), 5)

if __name__ == '__main__':
   unittest.main()
