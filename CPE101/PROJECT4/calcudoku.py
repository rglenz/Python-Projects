#Project 4
#Raymond Lenz and Jonathan Wallach 
#Instructor: S. Einakian
#Section: 9
#
#
#Test 1 takes about 55 seconds to get to the answer 
#
#
#PSUEDOCODE
#1. Initialize all cells to 0
#2. Increment the value in the current cell by 1 (starting from the top-left cell)
#    a. If the incremented value is greater than the maximum possible value, set the current cell to 0 and move back to the previous cell
#    b. Otherwise, check if the number is valid. If so, continue to the next cell to the right (advancing to the next row when necessary)
#3. Repeat Step 2 until the puzzle is fully populated and valid
#first we must create the info list which uses the transpose function from func_calcudoku to get the info for the cages
#next we will create the while loop that will cycle through every single combination of numbers in our puzzle
#in the while loop we will verify if things are valid
#lastly we need to create a for loop to print the list in the correct format
import func_calcudoku as f
import itertools as p
def main():
   #create a list filled with the cage information
   info=f.transpose()
   #create a 2d list that will represent our board
   puzzle=[0]*5
   #initialize all cells to 0
   for x in range(5):
      puzzle[x]=[0,0,0,0,0]
   cell=0
   while(cell<25):
      #determines what cell in the list will be modified 
      col=cell%5
      row=cell//5
      #increment the cell by 1
      puzzle[row][col]+=1
      #if the cell is out of bounds set it to 0 and move back
      if puzzle[row][col]>5:
         puzzle[row][col]=0
         cell-=1
      #if the cells are invalid for the cages set the current cell to 0 and move back
      elif f.validate_cages(puzzle,info)==False:
         puzzle[row][col]=0
         cell-=1
      #if the rows and columns are valid move to the next cell
      elif f.validate_rows(puzzle) and f.validate_cols(puzzle):
         cell+=1
      #if everything is valid end the loop because thats the answer
      elif f.validate_all(puzzle,info):
         break
     
      
#print the final answer correctly 
   for row in puzzle:
      cnt=0
      for item in row:
         if row.index(item)<=3:
            print(item,end=' ')
         else:
            print(item,end='')
         cnt+=1
         if cnt==5:
            print()

if __name__ == '__main__':
   main()




