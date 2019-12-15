# Project 2 - wordFinder
#
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9
import funcs
def main():
   puzzle=str(input())
   words=str(input())
   wordsList=words.split()
   rows,cols=funcs.formatPuzzle(puzzle)
   funcs.forward(wordsList,rows)
   funcs.backward(wordsList,rows)
   
   
   funcs.down(wordsList,cols)
      
   funcs.up(wordsList,cols)
   
if __name__ == '__main__':
   main() 
