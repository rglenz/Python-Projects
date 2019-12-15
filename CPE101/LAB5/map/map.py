#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9 

#function takes in a list and squares every item in the list 
# list -> list 
def square_all(l):
   square=list(map(lambda x:x**2,l))
   return square
#function takes in a list and a value and adds the value to every item in the list 
#list float -> list 
def add_n_all(l,j):
   for x in range(len(l)):
      l[x]=l[x]+j
   return l
# this function takes in a list and determines if the values in the list are true or false based off if they are odd or even 
# list -> list 
def even_or_odd_all(l):
   x=0
   while(x<len(l)):
      if l[x]%2==0:
         l[x]=True
      else:
         l[x]=False
      x=x+1
   return l

