import unittest
import filecmp
import subprocess
from concordance import *

class TestList(unittest.TestCase):
    
    def test_remove_punctuation(self):
        s='hi my-name\'s ray and i, dont: know how-to-use-grammar'
        ct=Concordance()
        s=ct.remove_punctuation(s)
        self.assertEqual(s,'hi my names ray and i dont know how to use grammar')
        s='hi my-name\'s ra*y (and) !!!i, dont: know how-to-use-gram+ma=r-'
        s=ct.remove_punctuation(s)
        self.assertEqual(s,'hi my names ray and i dont know how to use grammar ')
    def test_check_stop(self):
        ct=Concordance()
        ct.load_stop_table('stop_words.txt')
        self.assertTrue(ct.check_stop('a'))
        self.assertFalse(ct.check_stop('b'))
        self.assertTrue(ct.check_stop('only'))
        self.assertTrue(ct.check_stop('would'))
        self.assertTrue(ct.check_stop('your'))
        self.assertFalse(ct.check_stop('Ray'))
        self.assertFalse(ct.check_stop('yoyo'))
        self.assertFalse(ct.check_stop('wazzap'))
    def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(conc.check_stop('a'))
       self.assertTrue(conc.check_stop('would'))
       self.assertFalse(conc.check_stop('hello'))
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

    def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))
    def test_03(self):
       conc = Concordance()
       conc.load_stop_table("spec_stop.txt")
       conc.load_concordance_table("spec.txt")
       conc.write_concordance("spec_con.txt")
       self.assertTrue(filecmp.cmp("spec_con.txt", "spec_sol.txt"))
    def test_04(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       err = subprocess.call("diff -wb declaration_con.txt declaration_sol.txt", shell = True)
    def test_5(self):
        conc=Concordance()
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            conc.load_concordance_table("dne.txt")
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            conc.load_stop_table("dne.txt")
    def test_6(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("empty.txt")
       conc.write_concordance("empty_con.txt")
       self.assertTrue(filecmp.cmp("empty_con.txt", "empty_sol.txt"))

       
       
if __name__ == '__main__':
   unittest.main()
