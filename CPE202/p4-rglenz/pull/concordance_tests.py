import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

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
    def test_04(self):
       conc = Concordance()
       conc.load_stop_table("spec_stop.txt")
       conc.load_concordance_table("spec.txt")
       conc.write_concordance("spec_con.txt")
       self.assertTrue(filecmp.cmp("spec_con.txt", "spec_sol.txt"))

    

if __name__ == '__main__':
   unittest.main()
