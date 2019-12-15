
# Project 4
#
# Name: Raymond Lenz and Jonathan Wallach
# Instructor: S. Einakian
# Section: 9
#
#PSUEDOCODE!
#1. Initialize all cells to 0
#2. Increment the value in the current cell by 1 (starting from the top-left cell)
#    a. If the incremented value is greater than the maximum possible value, set the current cell to 0 and move back to the previous cell
#    b. Otherwise, check if the number is valid. If so, continue to the next cell to the right (advancing to the next row when necessary)
#3. Repeat Step 2 until the puzzle is fully populated and valid
#in order to do this we need 6 main functions
#one to create a list filled with the cage info and four others to do the checking for the puzzle
#for validation of the rows and columns the functions must ensure there are no duplicate numbers and ignore zeros
#validate cages must ensure that all of the populated cells in a cage add up to less than or equal to the cage sum
#validate all will ensure that all three of the validation functions are true
#ensure filled will make sure that the entire puzzle is populated and has no zero's




#this function will create a list of information regarding the cages
# -> list
def transpose():
   #create a 2 dimensional list of the information about the calcudoku puzzle
   cages=[]
   fin=int(input())
   for x in range(fin):
      temp=input().split()
      cages.append(temp)
   return cages

#this function ensures that there are no duplicate numbers in the rows 
#list -> bool
def validate_rows(grid):
   for i in range(len(grid)):
      for  x in range(5):
         for z in range(5):
            if grid[i][x]==grid[i][z] and x!=z and grid[i][x]>0:
               return(False)
   return(True)

#this function ensures that there are no duplicate numbers in the columns 
#list -> bool
def validate_cols(grid):
   for i in range(len(grid)):
      for x in range(len(grid)):
         for z in range(5):
            for w in range(5):
               if grid[z][x]==grid[w][x] and z!=w and grid[z][x]>0:
                  return(False)
   return(True)

#this function makes sure that the cage information is true. It makes sure that the cells involved with a cage dont exceed the maximum value 
#list list -> bool
def validate_cages(grid,cages):
   for x in range(len(cages)):
      Finalsum=int(cages[x][0])
      cagesum=0
      for y in range(1,len(cages[x])):
         col=int(cages[x][y])%5
         row=int(int(cages[x][y])/5)
         cagesum+=grid[row][col]
      if cagesum<=Finalsum:
         continue
      else:
         return False
   return True 

#this function ensures that all three of the checks are true 
#list list -> bool
def validate_all(grid, cages):
   row=validate_rows(grid)
   col=validate_cols(grid)
   cage=validate_cages(grid,cages)
   filled=ensure_filled(grid)
   if row and col and cage and filled == True:
      return True
   else:
      return False
# this function ensures that the whole puzzle is filled 
#list -> bool
def ensure_filled(grid):
   for x in range(len(grid)):
      for y in grid[x]:
         if y==0:
            return False
         else:
            continue
   return True

