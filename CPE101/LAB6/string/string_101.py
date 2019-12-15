#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9

#this function takes in a string and converts it to the corresponding string with rot 13 encryption 
#string->string
def str_rot_13(s):
   rotS=''
   for x in s: 
      num= ord(x)
      if ord('a')<=ord(x)<=ord('z'):
         for i in range(13):
            if num==ord('z'):
               num=ord('a')-1
            num=num+1
         rotS+=(chr(num))
      elif ord('A')<=ord(x)<=ord('Z'):
         for i in range(13):
            if num==ord('Z'):
               num=ord('A')-1
            num=num+1
         rotS+=(chr(num))
      else:
         rotS+=' '
   return(rotS)
#this function takes in a string replaces any instance of c1 with c2 then return the new translated string 
#string->string
def str_translate_101(s,c1,c2):
   sFinal=[c2 if x==c1 else x for x in s] 
   
   sFinal = ''.join(sFinal)
   return (sFinal)


      
