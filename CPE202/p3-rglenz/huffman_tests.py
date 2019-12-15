import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self):
        freqlist	= cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_01a_test_file1_parse_header(self):
        f = open('file1_compressed_soln.txt', 'rb')
        header = f.readline()        
        f.close()
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.compare_freq_counts(parse_header(header), expected)
        
    def test_01_test_file1_decode(self):
        huffman_decode("file1_compressed_soln.txt", "file1_decoded.txt")
        err = subprocess.call("diff -wb file1.txt file1_decoded.txt", shell = True)
        self.assertEqual(err, 0)
    def test_02_test_file2_decode(self):
        huffman_decode("file2_compressed_soln.txt", "file2_decoded.txt")
        err = subprocess.call("diff -wb file2.txt file2_decoded.txt", shell = True)
        self.assertEqual(err, 0)
    def test_3_test_multiline_decode(self):
        huffman_decode("multiline_compressed_soln.txt", "multiline_decoded.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decoded.txt", shell = True)
        self.assertEqual(err, 0)
    def test_4_test_empty_decode(self):
        huffman_decode("empty1o_compressed.txt", "empty1_decoded.txt")
        err = subprocess.call("diff -wb empty1.txt empty1_decoded.txt", shell = True)
        self.assertEqual(err, 0)
    def test_5_test_single_decode(self):
        huffman_decode("singlecharo_compressed.txt", "singlechar_decoded.txt")
        err = subprocess.call("diff -wb singlechar.txt singlechar_decoded.txt", shell = True)
        self.assertEqual(err, 0)

    def compare_freq_counts(self, freq, exp):
        for i in range(256):
            stu = 'Frequency for ASCII ' + str(i) + ': ' + str(freq[i])
            ins = 'Frequency for ASCII ' + str(i) + ': ' + str(exp[i])
            self.assertEqual(stu, ins)
                
    def test_cnt_freq_01(self):
        freqlist	= cnt_freq("empty.txt")
        anslist = [0]*256
        self.assertListEqual(freqlist, anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)
    def test_create_huff_tree_01(self):
        freqlist = [0]*256
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree,None)
    def test_create_huff_tree_02(self):
        freqlist = [0]*256
        freqlist[1]=1
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.left,None)
        self.assertEqual(hufftree.right,None)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")
    def test_create_header_01(self):
        freqlist = cnt_freq("declaration.txt")
        self.assertEqual(create_header(freqlist), "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')
    def test_create_code_01(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord(' ')], '00')
        self.assertEqual(codes[ord('b')], '01')
    def test_create_code_03(self):
        freqlist = cnt_freq("test.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')
    
    
    def test_comes_before(self):
        a=HuffmanNode(32,100)
        b=HuffmanNode(98,100)
        self.assertTrue(comes_before(a,b))
        self.assertFalse(comes_before(b,a))
        a=HuffmanNode(97,100)
        b=HuffmanNode(98,1000)
        self.assertTrue(comes_before(a,b))
        self.assertFalse(comes_before(b,a))
        b=HuffmanNode(99,1)
        self.assertTrue(comes_before(b,a))
        c=HuffmanNode(10,2)
        d=HuffmanNode(9,2)
        self.assertFalse(comes_before(c,d))

    def test_combine(self):
        a=HuffmanNode(10,2)
        b=HuffmanNode(12,16)
        node=combine(a,b)
        self.assertEqual(node.char,10)
        self.assertEqual(node.freq,18)
        a=HuffmanNode(10,16)
        b=HuffmanNode(11,2)
        node=combine(a,b)
        self.assertEqual(node.char,10)
        self.assertEqual(node.freq,18)
        c=HuffmanNode(10,2)
        d=HuffmanNode(9,2)
        node=combine(c,d)
        self.assertEqual(node.char,9)
        self.assertEqual(node.freq,4)


    def test_encode(self):
        huffman_encode("file1.txt",'file1o.txt')
        sol= open('file1o.txt','r')
        out= open('file1_soln.txt','r')
        sollst=[]
        outlst=[]
        for line in sol:
            sollst.append(line)
        for line in out:
            outlst.append(line)
        sol.close()
        out.close()
        self.assertEqual(sollst,outlst)
    def test_encode_01(self):
        huffman_encode("file2.txt",'file2o.txt')
        sol= open('file2o.txt','r')
        out= open('file2_soln.txt','r')
        sollst=[]
        outlst=[]
        for line in sol:
            sollst.append(line)
        for line in out:
            outlst.append(line)
        sol.close()
        out.close()
        self.assertEqual(sollst,outlst)
    def test_encode_02(self):
        huffman_encode("multiline.txt",'multilineo.txt')
        sol= open('multilineo.txt','r')
        out= open('multiline_soln.txt','r')
        sollst=[]
        outlst=[]
        for line in sol:
            sollst.append(line)
        for line in out:
            outlst.append(line)
        sol.close()
        out.close()
        self.assertEqual(sollst,outlst)
    def test_encode_03(self):
        huffman_encode("declaration.txt",'declarationo.txt')
        sol= open('declarationo.txt','r')
        out= open('declaration_soln.txt','r')
        sollst=[]
        outlst=[]
        for line in sol:
            sollst.append(line)
        for line in out:
            outlst.append(line)
        sol.close()
        out.close()
        self.assertEqual(sollst,outlst)
    def test_encode_04(self):
        huffman_encode("singlechar.txt",'singlecharo.txt')
        out= open('singlecharo.txt','r')
        outlst=[]
        for line in out:
            outlst.append(line)
        out.close()
        self.assertEqual(outlst,['97 7\n'])
    def test_encode_05(self):
        huffman_encode("empty1.txt",'empty1o.txt')
        out= open('empty1.txt','r')
        outlst=[]
        for line in out:
            outlst.append(line)
        out.close()
        self.assertEqual(outlst,[])
    def test_encode_06(self):
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            huffman_encode("dne.txt",'empty1o.txt')
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            cnt_freq("dne.txt")
        with self.assertRaises(FileNotFoundError):  # used to check for exception
            huffman_decode("dne.txt","blah.txt")
if __name__ == '__main__': 
   unittest.main()
