# Project 3
#
# Name: Raymond Lenz and Jonathan Wallach
# Instructor: S. Einakian
# Section: 9
'''
Some of the suggested functions are shown bellow.
You can create as many functions as you need.
You can even ignore the suggested functions.
But you are not allow to write the whole project in One Function!
'''
#1) gets input for puzzle
def formatPuzzle(s):
   puzzle= s
   print (puzzle)
   rows=[]
   cols=[]
   colTemp=[]
#creates a list with 10 elements. Each element is a row
   for idx in range(0,len(puzzle),10):
      row=puzzle[idx:idx+10]
      rows.append(row)
   rows.pop()
#creates a string with the order of the columns from the row list
   for idx in range(0,len(rows)):
      for x in range(0,10):
         colTemp.append(rows[x][idx])
   stringCols=''.join(colTemp)
#creates another list with 10 elements. Each element is a column
   for idx in range(0,len(stringCols),10):
      col=stringCols[idx:idx+10]
      cols.append(col)
   print('Puzzle:')
   print('')
   for x in range(0,len(rows)):
      print (rows[x])
   return rows,cols


# 2) checks forward for given word
def forward(wordList,rows):
   # Checks every word
   check = False
   for i in range(len(wordList)):
      # Checks every row
      for x in range(10):
         if wordList[i] in rows[x]:
            for y in range(10):
               if rows[x][y]==wordList[i][0]:
                  if y + len(wordList[i])<10:
                     check=True
               while check==True:
                  for z in range(len(wordList[i])):
                     if rows[x][y+z]==wordList[i][z] and z==len(wordList[i])-1:
                        print(wordList[i],': (FORWARD) ''Row: ',x,' column:',y)
                        check=False
                     else:
                        check=False

 
#3) checks backward for given word
def backward(wordList,rows):
   # Checks every word
   check = False
   rows.reverse()
   for x in range (0,len(rows)):
      rows[x]=rows[x][::-1]
   for i in range(len(wordList)):
      # Checks every row
      for x in range(10):
         if wordList[i] in rows[x]:
            for y in range(10):
               if rows[x][y]==wordList[i][0]:
                  if y + len(wordList[i])<10:
                     check=True
               while check==True:
                  for z in range(len(wordList[i])):
                     if rows[x][y+z]==wordList[i][z] and z==len(wordList[i])-1:
                        print(wordList[i],': (BACKWARDS) ''Row: ',9-x,' column:',9-y)
                        check=False
                     else:
                        check=False

#4) checks up for given word
def up(wordList,cols):
   # Checks every word
   print('MADE IT HERE')
   check = False
   cols.reverse()
   for x in range (0,len(cols)):
      cols[x]=cols[x][::-1]
   for i in range(len(wordList)):
      # Checks every row
      for x in range(10):
         if wordList[i] in cols[x]:
            print('made it here')
            for y in range(10):
               print('made it here')
               if cols[x][y]==wordList[i][0]:
                  print('made it')
                  if y + len(wordList[i])<10:
                     print('made')
                     check=True
                     while check==True:
                        for z in range(len(wordList[i])):
                           if cols[x][y+z]==wordList[i][z] and z==len(wordList[i])-1:
                              print(wordList[i],': (UP) ''Row: ',9-y,' column:',9-x)
                              check=False
                           else:
                              check=False


#5) checks down for given word
def down(wordList,cols):
   # Checks every word
   check = False
   for i in range(len(wordList)):
      # Checks every row
      for x in range(10):
         if wordList[i] in cols[x]:
            for y in range(10):
             if cols[x][y]==wordList[i][0]:
                  if y + len(wordList[i])<10:
                     check=True
                     while check==True:
                        for z in range(len(wordList[i])):
                           if cols[x][y+z]==wordList[i][z] and z==len(wordList[i])-1:
                              print(wordList[i],': (DOWN) ''Row: ',y,' column:',x)
                              check=False
                        else:
                           check=False


