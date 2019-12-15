#Lab 4
#
#Name: Raymond Lenz
#Instructor: Sussan Einakian 
#Section: 9

import driver 

def letter(row,col):
   if 2<=row<=3 and 3<col<10:
      return 'Z'
   elif 4<=row<=5 and 4<=col<=6:
      return 'Z'
   elif 4<=row<=5 and 7<=col<=9:
      return 'X'
   elif 4<=row<=5 and 10<=col<=12:
      return 'B'
   elif row==6 and 7<=col<=12:
      return 'B'
   else:
      return 'T'



if __name__ == '__main__':
        driver.comparePatterns(letter)
