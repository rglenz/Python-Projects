# Lab 4
#
# Name: Raymond Lenz
# Instructor: Sussan Einakian
# Section: 9

import driver

def letter(row, col):
   if row>col:	
      return 'T'
   else:
      return 'W'

if __name__ == '__main__':
	driver.comparePatterns(letter)
