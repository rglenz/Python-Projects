#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9 

#Function will add two lists together and make them into one 
#list list -> list 
def poly_add2(list1,list2):
   addList = [list1[0]+list2[0],list1[1]+list2[1],list1[2]+list2[2]]
   return list(addList)
# function will multiply two lists together and create one 
#list list -> list 
def poly_mult2(list1,list2):
   multList = [list1[0]*list2[0],list1[0]*list2[1]+list2[0]*list1[1],list1[1]*list2[1]]
   return list(multList)


