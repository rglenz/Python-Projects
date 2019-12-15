from huffman_bit_writer import *
from huffman_bit_reader import *
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right
    #used for sorting 
    def __lt__(self,other):
        return comes_before(self,other)
    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node
#checks to see if huffman node should come before another in the tree
def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    #checks frequencies
    if a.freq<b.freq:
        return True
    elif a.freq>b.freq:
        return False
    elif a.freq==b.freq:
        #checks which is the smaller character
        if a.char<b.char:
            return True
        return False

#combines two huffman nodes
def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    #determines what order to combine
    f=a.freq+b.freq
    if comes_before(a,b)==True and a.char<b.char:
        newNode=HuffmanNode(a.char,f)
        newNode.set_left(a)
        newNode.set_right(b)
    elif comes_before(a,b)==True and b.char<a.char:
            newNode=HuffmanNode(b.char,f)
            newNode.set_left(a)
            newNode.set_right(b)
    else:
        if a.char<b.char:
            newNode=HuffmanNode(a.char,f)
            newNode.set_left(b)
            newNode.set_right(a)
        else:
            newNode=HuffmanNode(b.char,f)
            newNode.set_left(b)
            newNode.set_right(a)
    return newNode

#counts every single character in a file and keeps track by incrementing its spot in the list 
def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    #creates a base list of all 8 bit chars
    lst=[0]*256
    try:
        f= open(filename,'r')
    except:
        raise FileNotFoundError
    for line in f:
        for chr in line:
            num=ord(chr)
            #increment 
            lst[num]=lst[num]+1
    f.close()
    return lst

#creates a huffman tree based on the frequencies and algorithm we learned in class
def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    leaflst=[]
    #handles empty file 
    if char_freq==[0]*256:
        return None
    #for every character a new huffman node is created 
    for x in range(len(char_freq)):
        if char_freq[x]!=0:
            leaflst.append(HuffmanNode(x,char_freq[x]))
    #list gets sorted and then algorithm is applied 
    while len(leaflst)>1:
        leaflst.sort() 
        a=leaflst.pop(0)
        b=leaflst.pop(0)
        leaflst.append(combine(a,b))    
    return leaflst.pop(0)

#creates the actual codes for each character and stores them in a list 
def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    lst=['']*256
    c=''
    return create_code_helper(node,lst,c)

#recursively creates the character codes by adding a 0 or 1 depending on traversing left or right 
def create_code_helper(node, lst,c):
    if node is not None:
        create_code_helper(node.left,lst,c+'0')
        #if the node is a leaf add c to the list and start over 
        if node.left is None and node.right is None:
            lst[node.char]=c
        create_code_helper(node.right,lst,c+'1') 
    return lst
    
#creates the header for the files based off of the frequency information     
def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    headlst=[]
    for x in range(len(freqs)):
        if freqs[x]!=0:
            headlst.append((x,freqs[x]))
    header=''
    for item in headlst:
        header+=str(item[0])+' '+str(item[1])+' '
    #get rid of extra space at the end 
    return header[:-1]

#creates an out file and a compressed out file that is the translated in file 
def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters - both files will have .txt extensions
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Also creates a second output file which adds _compressed before the .txt extension to the name of the file.
    This second file is actually compressed by writing individual 0 and 1 bits to the file using the utility methods 
    provided in the huffman_bits_io module to write both the header and bits.
    Take not of special cases - empty file and file with only one unique character"""
    #handles if the file does not exist 
    try:
        i= open(in_file,'r')
        o= open(out_file,'w')
    except:
        raise FileNotFoundError
    #call all of the functions 
    freq=cnt_freq(in_file)
    tree=create_huff_tree(freq)
    head=create_header(freq)
    code=create_code(tree)
    bwriter=HuffmanBitWriter(out_file[:-4]+'_compressed.txt')
    #write in the header
    if head!="":
        o.write(head+"\n")
        #create the compressed file
        #write compressed header 
        bwriter.write_str(head+"\n")
    #write the body 
    for line in i:
        for chr in line:
            c=ord(chr)
            bwriter.write_code(code[c])
            o.write(code[c])
    o.close()
    i.close()
    bwriter.close()
#create freq list from the header 
def parse_header(header_string):
    head_lst=header_string.split()
    #create freq list
    freqlst=[0]*256
    #for every even value store the next value in the list at the even values index
    for x in range(len(head_lst)):
        if x%2!=0:
            freqlst[int(head_lst[x-1])]=(int(head_lst[x]))
    return freqlst
#create a decoded file from an encoded file of bits 
def huffman_decode(encoded_file, decode_file):
    #handles file not found 
    try:
        decode=open(decode_file,'w')
        encode=HuffmanBitReader(encoded_file)
    except:
        raise FileNotFoundError
    #create freq list and then tree
    head=encode.read_str()
    parsed=parse_header(head)
    tree=create_huff_tree(parsed)
    code=create_code(tree)
    node=tree
    cnt=0
    #traverse tree and print out a character for the amount of frequencies total 
    if tree is not None:
        while cnt<tree.freq:
            if node.left is None and node.right is None:
                #write the file 
                decode.write(chr(node.char))
                #increase the count signaling that a character has been written
                cnt=cnt+1
                #start back at the top of the tree
                node=tree
            elif encode.read_bit():
                node=node.right
            else:
                node=node.left
    decode.close()
    encode.close()

    
