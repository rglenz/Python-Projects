 # Lab 4
#
# Name: Raymond Lenz
# Instructor: Sussan Einakian
# Section: 9

import driver

def letter(row, col):
   if row<=9:	
      return 'R'
   else:
      return 'Q'

if __name__ == '__main__':
	driver.comparePatterns(letter)
