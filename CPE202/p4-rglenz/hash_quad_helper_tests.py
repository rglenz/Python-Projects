import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_quadratic_probe(self):
        ht = HashTable(15)
        ht.insert("catattack", 6)
        ht.insert("catattack1111", 0)
        ht.insert("catattack2222", 1)
        ht.insert("catattack3333", 1)
        self.assertEqual(ht.quadratic_probe("catattack"), 12)
        self.assertEqual(ht.quadratic_probe("catattack1111"), 13)
        self.assertEqual(ht.quadratic_probe("catattack2222"), 1)
        self.assertEqual(ht.quadratic_probe("catattack3333"), 6)
    def test_bigger_table(self):
        ht=HashTable(3)
        ht.hash_table=[('hi',1),('my',2),None]
        ht.num_items=2
        ht.bigger_table(ht.hash_table)
        self.assertEqual(ht.hash_table,[('my',2),None,None,None,('hi',1),None,None])
    def test_bigger_table_01(self):
        ht=HashTable(191)
        ht.bigger_table(ht.hash_table)
        self.assertEqual(ht.get_table_size(),383)

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 6)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert('cow','y')
        ht.insert('cow',3.14)
        ht.insert('chicken',[1,2,3])
        ht.insert('chicken',(1,2,3))
        self.assertEqual(ht.get_value('chicken'),(1,2,3))
        self.assertEqual(ht.get_num_items(), 3)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])


    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.in_table("cat1"), False)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)
    def test_02g(self):
        ht = HashTable(7)
        ht.insert("catattack", 6)
        ht.insert("catattack1243", 0)
        ht.insert("catattack12345", 1)
        
        self.assertEqual(ht.get_index("catattack"), 6)
        self.assertEqual(ht.get_index("catattack1243"), 0)
        self.assertEqual(ht.get_index("catattack12345"), 3)
    def test_03g(self):
        ht = HashTable(7)
        ht.insert("ABCDEFGH1", 9)
        ht.insert("ABCDEFGH2", 0)
        ht.insert("ABCDEFGH3", 1)
        ht.insert("ABCDEFGH4", 1)
       
        self.assertEqual(ht.get_index("ABCDEFGH1"), 2)
        self.assertEqual(ht.get_index("ABCDEFGH2"), 8)
        self.assertEqual(ht.quadratic_probe("ABCDEFGH2"), 8)
        self.assertEqual(ht.get_index("ABCDEFGH3"), 12)
        self.assertEqual(ht.get_index("ABCDEFGH4"), 9)
        self.assertEqual(ht.get_value("ABCDEFGH1"), 9)
        self.assertEqual(ht.get_value("ABCDEFGH2"), 0)
        self.assertEqual(ht.get_value("ABCDEFGH3"), 1)
        self.assertEqual(ht.get_value("ABCDEFGH4"), 1)
        self.assertEqual(ht.in_table("ABCDEFGH4"), True)
        self.assertEqual(ht.in_table("ABCDEFGH2"), True)
    def test_10(self):
        ht = HashTable(7)
        ht.insert("cat", 1)
        ht.insert("dog", 2)
        ht.insert("rat", 3)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.horner_hash('cat'),3)
        self.assertEqual(ht.get_index('cat'),3)
        self.assertEqual(ht.get_value('cat'), 1)
        self.assertAlmostEqual(ht.get_load_factor(), 3/7)
        ht.insert("mouse", 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertEqual(ht.horner_hash('cat'),12)
        self.assertEqual(ht.get_index('cat'),12)
        self.assertEqual(ht.get_value('cat'),1)
        self.assertEqual(ht.horner_hash('dog'),14)
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.in_table("cat1"), False)
        self.assertEqual(ht.get_num_items(), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 4/15)
    def test_11(self):
        ht = HashTable(7)
        ht.insert("ABCDEFGH1", 9)
        ht.insert("ABCDEFGH2", 0)
        ht.insert("ABCDEFGH3", 1)
        ht.insert("ABCDEFGH4", 1)
        ht.insert("ABCDEFGH3", 2)
        ht.insert("ABCDEFGH4", 2)
        self.assertEqual(ht.get_index("ABCDEFGH1"), 2)
        self.assertEqual(ht.get_index("ABCDEFGH1hiiiiii"), None)
        self.assertEqual(ht.get_index("ABCDEFGH2"), 8)
        self.assertEqual(ht.quadratic_probe("ABCDEFGH2"), 8)
        self.assertEqual(ht.get_index("ABCDEFGH3"), 12)
        self.assertEqual(ht.get_index("ABCDEFGH4"), 9)
        self.assertEqual(ht.get_value("ABCDEFGH1"), 9)
        self.assertEqual(ht.get_value("A"), None)
        self.assertEqual(ht.get_value("ABCDEFGHGJGHG"), None)
        self.assertEqual(ht.get_value("ABCDEFGH2"), 0)
        self.assertEqual(ht.get_value("ABCDEFGH3"), 2)
        self.assertEqual(ht.get_value("ABCDEFGH4"), 2)
        self.assertEqual(ht.in_table("ABCDEFGH4"), True)
        self.assertEqual(ht.in_table("ABCDEFGH2"), True)
        self.assertEqual(ht.in_table("ABCDEFGH2HI"), False)
    def test_12(self):
        ht = HashTable(191)
        ht.insert("A", 9)
        ht.insert("B", 0)
        ht.insert("C", 1)
        ht.insert("D", 1)
        ht.insert("E", 2)
        ht.insert("F", 2)
        keys=ht.get_all_keys()
        self.assertEqual(keys,['A','B','C','D','E','F'])
        self.assertEqual(ht.get_index('HEllo'),None)


if __name__ == '__main__':
   unittest.main()
