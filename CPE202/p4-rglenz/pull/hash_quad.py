class HashTable:

    def __init__(self, table_size=191):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value=None):
        ''' Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is any object (e.g. Python List).
        If the key is not already in the table, the key is inserted along with the associated value
        If the key is is in the table, the new value replaces the existing value.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1).'''
        #the index is the hash of the Key 
        i=self.horner_hash(key)
        #insert if the table at this index holds nothing
        if self.hash_table[i] is None:
            self.hash_table[i]=[key,[value]]
        #if it holds the same key update the value 
        elif self.hash_table[i][0]==key:
            if value not in self.hash_table[i][1]:
                self.hash_table[i][1]=self.hash_table[i][1].append(value)
        #if it holds a different key use quadratic probing to find the right spot 
        elif self.hash_table[i][0]!=key:
            if self.hash_table[self.quadratic_probe(key)] is not None:
                if value not in self.hash_table[self.quadratic_probe(key)][1]:
                    self.hash_table[self.quadratic_probe(key)][1].append(value)
            else:
                self.hash_table[self.quadratic_probe(key)]=[key,[value]]
        #check the load factor 
        self.num_items+=1
        load=self.get_load_factor()
        #if load factor larger than .5 increase the size of the table
        if load>0.5:
            self.bigger_table(self.hash_table)
    
    def quadratic_probe(self,key):
        quad=0
        idx=self.horner_hash(key)
        h=self.horner_hash(key)
        while self.hash_table[idx] is not None and self.hash_table[idx][0]!=key:
            quad+=1
            idx=(h+(quad**2))%self.table_size
        return idx
        
           
            
    def bigger_table(self,table):
        new=HashTable(self.table_size*2+1)
        for item in table:
            if item is not None:
                for line in item[1]:
                    new.insert(item[0],line)
        self.hash_table=new.hash_table
        self.table_size=new.table_size
        self.num_items=new.num_items


    def horner_hash(self, key):
        ''' Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification.'''
        tot=0
        #if the string is longer than 8 characters just utilize the first 8 
        n=min(8,len(key))
        #perform hash 
        for i in range (n):
            tot+=ord(key[i])*31**(n-1-i)
        tot=tot%self.get_table_size()
        return tot

    def in_table(self, key):
        ''' Returns True if key is in an entry of the hash table, False otherwise.'''
        #get the hash of the key 
        i=self.horner_hash(key)
        #check if the key is in the hash table 
        if self.hash_table[i] is None:
            return False
        if key == self.hash_table[i][0]:
            return True
        if key != self.hash_table[i][0]:
            newi=self.quadratic_probe(key)
            if self.hash_table[newi] is None:
                return False
            if key == self.hash_table[newi][0]:
                return True
        return False
      

    def get_index(self, key):
        ''' Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None.'''
        i=self.horner_hash(key)
        if self.hash_table[i] is None:
                return None
        if self.hash_table[i][0]==key:
            return i
        elif self.hash_table[i][0]!=key:
            newi=self.quadratic_probe(key)
            if self.hash_table[newi] is not None and self.hash_table[newi][0]==key :
                return newi
            return None
                

    def get_all_keys(self):
        ''' Returns a Python list of all keys in the hash table.'''
        keys=[]
        for item in self.hash_table:
            if item is not None:
                keys.append(item[0])
        return keys

    def get_value(self, key):
        ''' Returns the value associated with the key. 
        If key is not in hash table, returns None.'''
        i=self.horner_hash(key)
        quad=0
        if self.hash_table[i] is None:
            return None
        if self.hash_table[i][0]==key:
            return self.hash_table[i][1]
        elif self.hash_table[i][0]!=key:
            newi=self.quadratic_probe(key)
            if self.hash_table[newi] is None:
                return None
            return self.hash_table[newi][1]
    
    def get_num_items(self):
        ''' Returns the number of entries in the table.'''
        return self.num_items

    def get_table_size(self):
        ''' Returns the size of the hash table.'''
        return self.table_size

    def get_load_factor(self):
        ''' Returns the load factor of the hash table (entries / table_size).'''
        return self.get_num_items()/self.get_table_size()
