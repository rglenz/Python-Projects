 # Lab 4
#
# Name: Raymond Lenz
# Instructor: Sussan Einakian
# Section: 9

import driver

def letter(row, col):	
   if row==9 and col==9:
      return 'Z'
   else:
      return 'G'

if __name__ == '__main__':
	driver.comparePatterns(letter)
