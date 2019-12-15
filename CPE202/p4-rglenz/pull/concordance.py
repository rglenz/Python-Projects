from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            stop=open(filename,'r')
        except:
            raise FileNotFoundError
        stop_table=HashTable()
        for line in stop:
            stop_table.insert(line.rstrip(),0)
        self.stop_table=stop_table
        stop.close()

    def remove_punctuation(self,line):
        for chr in line:
            if chr == '-':
                line=line.replace(chr,' ')
            if chr in string.punctuation:
                line=line.replace(chr,'') 
        return line
        
    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        #handles if the file does not exist 
        try:
            f=open(filename,'r')
        except:
            raise FileNotFoundError
        conc_table=HashTable()
        numline=0
        for line in f:
            numline+=1
            line=self.remove_punctuation(line)
            line=line.split()
            for word in line:
                #remove all numbers 
                try:
                    float(word)
                except:    
                    
                    conc_table.insert((word.rstrip()).lower(),numline)
           
        self.concordance_table=conc_table
        f.close()
    
    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        f=open(filename,'w')
        keys=self.concordance_table.get_all_keys()
        keys.sort()
        for i in range(len(keys)):
            #write the value to the out file 
            
            if not self.check_stop(keys[i]):
                f.write(str(keys[i])+': '+str(self.concordance_table.get_value(keys[i])))
                #go to the next line every time except on the last value 
                if i != len(keys)-1 :
                    f.write('\n')
        f.close()


    

    #checks to see if a word is in the stop table 
    def check_stop(self,word):
        if self.stop_table.in_table(word) :
            return True
        return False
        
