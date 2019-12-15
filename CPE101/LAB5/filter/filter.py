#Raymond Lenz
#Instructor: Sussan Einakian 
#Section: 9 

#this function filters a list and returns a list that only contains the positive values of the first list 
# list -> list 
def are_positive(l):
   l2=filter(lambda x: x%2==0,l)
   return (list(l2))
#This function takes in a list and a value and returns a list that only contains the items of the first list that are greater than the value 
#list int -> list
def are_greater_than_n(l,n):
   l2=[]
   l2=[x for x in l if x>n]
   return (l2)
#this funciton takes in a list and a value and returns a new list containing only the items of the first list that are divisible by the value 
# list int -> list 
def are_divisible_by_n(l,n):
   x=0
   l2=[]
   while len(l)>x:
      if l[x]%n==0:
         l2.append(l[x])
      x=x+1
   return (list(l2))


   
