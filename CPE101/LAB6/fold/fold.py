#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9

#This function takes in a list and adds all the elements in the list together and returns the sum 
#list -> int 
def sum(l):
   s=0
   for x in range (0,len(l)):
      if type(l[x])==int:
         s+=l[x]
      elif type(l[x])==list:
         for y in range(0,len(l[x])):
            s+=l[x][y]
   return s

#This function takes in a list and returns the index of the smallest value 
# list -> int
def index_of_smallest(l): 
   if len(l)<=0:
      idx=-1
      return (idx)
   elif type(l[0])==list:
      for y in range(0,len(l[0])):
         temp=l[0][y]
         if temp<idx:
            idx=temp
   else:  
      idx=l[0]
      temp=0
      for x in range(1,len(l)):
         if type(l[x])==list:
            for y in range(0,len(l[x])):
               temp=l[x][y]
               if temp<idx:
                  idx=temp
            index=x
         else:
            temp=l[x]
            if temp<idx:
               idx=temp
               index=l.index(idx)
      return (index)

