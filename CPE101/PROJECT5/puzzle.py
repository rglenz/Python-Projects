#Project 5
#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9
#
#
#
#PSEUDOCODE:
#I am going to create 3 functions to unscramble the puzzle.
#First will be the createList function which will take in the lines of the ppm file and return a list of all the pixels.
#The next function will shift the red values of each pixel and then update the green and blue pixels to show the hidden image.
#The last function will be a writeOut function which will take in the list of updated pixels and write them out to a file called blur with the PPM format.
#
#
#
#This function creates the list of values from the PPM file so that they can be manipulated
#list->list
def createList(lines):
    finall=[]
    linl=[]
    cnt=0
    for x in range(3,len(lines)):
        linl.append(lines[x].strip())
        cnt+=1
        if cnt==3:
            finall.append(linl)
            linl=[]
            cnt=0
    if linl==[]:
        pass
    else:
            finall.append(linl)
    return(finall)
#This function will manipulate the pixels of the puzzle image to decode it 
#list->
def shiftRed(finall):
    for pixel in finall:
    
        pixel[0]=int(pixel[0])*10
        if int(pixel[0])>255:
            pixel[0]=255
        if len(pixel)==3:
           pixel[1]=int(pixel[0])
           pixel[2]=int(pixel[0])
#This file will write the output to a PPM file 
#list list->
def writeOut(lines,finall):
    fout=open('hidden.ppm','w')
    fout.write(str(lines[0]))
    fout.write(str(lines[1]))
    fout.write(str(lines[2]))
    for x in finall:
       for y in x:
           fout.write(str(y)+'\n')




