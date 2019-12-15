#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9

#this function takes in a character and determines if it is lowercase 
#char->bool
def is_lower_101(a):
   x=ord(a)
   if ord('a')<=x<=ord('z'):
      return True 
   else:
      return False
#this function takes in a character and applies the rot 13 encryption scheme on it 
#char->char
def char_rot13(a):
   x= ord(a)
   if a.isupper():
      for i in range(13):
         if x==ord('Z'):
            x=ord('A')-1
         x=x+1
      return(chr(x))
   else:
      for i in range(13):
         if x==ord('z'):
            x=ord('a')-1
         x=x+1
      return(chr(x))



