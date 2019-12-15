#Project 5
#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9
#
#
#
#PSEUDOCODE:
#I am going to create 4 functions to complete the fade.
#First will be the createList function which will take in the lines of the ppm file and return a list of all the pixels.
#The next function will find the distance from the current pixel to the one we are fading around.
#To do this I used the distance Formula.
#The next function will actually create the fade effect.
#It will adjust the RGB values for every pixel based on the spec and give the Image a nice fade look.
#The last function will be a writeOut function which will take in the list of updated pixels and write them out to a file called blur with the PPM format.
#
#
#
import math

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
#This function calculates the distance from the current pixel to the pixel we are fading from
#int int int int-> int
def distCalc(pr,pc,r,c,):
    distance=math.sqrt(((pr-r)*(pr-r))+((pc-c)*(pc-c)))
    return distance
#This function takes in all the necessary components needed to compute the fade for each pixel of the PPM file
#list int int int int ->
def computeFade(finall,numrows,numcols,row,col,rad):
    for x in range(len(finall)):
        for y in range(3):
            dist=distCalc(x%numrows,x//numcols,row,col)
            newval=(rad-dist)/rad
            if newval<.2:
                newval=.2
            finall[x][y]=round(int(finall[x][y])*newval)
            if finall[x][y]>255:
                finall[x][y]=255
            elif finall[x][y]<0:
                finall[x][y]=0
#This file will write the output to a PPM file 
#list list->
def writeOut(lines,finall):
    fout=open('fade.ppm','w')
    fout.write(str(lines[0]))
    fout.write(str(lines[1]))
    fout.write(str(lines[2]))
    for x in finall:
        for y in x:
            fout.write(str(y)+'\n')