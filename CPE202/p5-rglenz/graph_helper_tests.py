import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
   
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())
    def test_03(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
    def test_04(self):
        g = Graph('test4.txt')
        self.assertEqual(g.conn_components(), [['v10', 'v11', 'v12', 'v13'],['v4', 'v6', 'v7', 'v8']])
        self.assertTrue(g.is_bipartite())
    def test_05(self):
        g = Graph('test5.txt')
        self.assertTrue(g.is_bipartite())
    def test_06(self):
        g = Graph('test6.txt')
        self.assertEqual(g.conn_components(), [['a', 'b', 'c', 'd']])
        self.assertTrue(g.is_bipartite())
    def test_07(self):
        g = Graph('test7.txt')
        self.assertEqual(g.conn_components(), [['0','1'],['a', 'b', 'c',]])
        self.assertFalse(g.is_bipartite())
    def test_08(self):
        g = Graph('test8.txt')
        self.assertFalse(g.is_bipartite())
    def test_09(self):
        g = Graph('test9.txt')
        self.assertTrue(g.is_bipartite())
    def test_10(self):
        g = Graph('test10.txt')
        self.assertEqual(g.conn_components(), [['1', '2', '3', '4', '5', '6', '7']])
        self.assertTrue(g.is_bipartite())

 


   
    def test_addVert(self):
        g = Graph('test2.txt')
        self.assertEqual(g.add_vertex('hi'),None)
    def test_keys(self):
        g = Graph('test2.txt')
        self.assertEqual(g.get_vertices(),['v1', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8'])
    def test_getVert(self):
        g = Graph('test2.txt')
        self.assertEqual(g.get_vertex('hi'),None)
        self.assertEqual(g.get_vertex('v1'),g.vertlst['v1'])
    

   
if __name__ == '__main__':
   unittest.main()
