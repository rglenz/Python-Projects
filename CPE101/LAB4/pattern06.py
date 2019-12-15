#Lab 4
#Name: Raymond Lenz 
#Instructor: Sussan Einakian
#Section: 9

import driver

def letter(row,col):
   if row==col:
      return 'X'
   elif row + col ==6: 
      return 'X'
   else:
      return 'O'
if __name__ == '__main__':
        driver.comparePatterns(letter) 
