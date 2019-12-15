#Project 5
#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9
import sys 
import puzzle
import fade
import blur
newl=sys.argv
#
#
#
#PSEUDOCODE:
#For the main file I am going to use an if else statement to check how many parameters are passed.
#If the correct amount is passed I will then create the necessary variables for either blur fade or puzzle and run the functions.
#lastly I will print out the new pixels to the files.
#
#
#
#determine what program to run based on number of command line arguments 
#test for fade
if len(newl)==5:
#Run Fade
    try:
        row=int(newl[2])
        col=int(newl[3])
        rad=int(newl[4])
        info=open(newl[1])
        lines=info.readlines()
        finall=fade.createList(lines)
        rc=lines[1].split()
        numrows=int(rc[0])
        numcols=int(rc[1])
        #Fade the picture
        fade.computeFade(finall,numrows,numcols,row,col,rad)
        #write it out to fade.ppm
        fade.writeOut(lines,finall)
    except IOError:
        print("Unable to open "+newl[1])
        quit
    except ValueError:
        print("Usage: python3 fade.py <image> <row> <column> <radius>")
        quit
#test for puzzle
elif len(newl)==2:
#run puzzle 
    try:
        info=open(newl[1])
        lines=info.readlines()
        finall=puzzle.createList(lines)
        #decode
        puzzle.shiftRed(finall)
        #Write it out to hidden.ppm
        puzzle.writeOut(lines,finall)
    except IOError:
        print("Unable to open "+newl[1])
        quit
#test for blur   
elif len(newl)==3:
    try:
        info=open(newl[1])
        lines=info.readlines()
        finall=blur.createList(lines)
        rc=lines[1].split()
        numrows=int(rc[1])
        numcols=int(rc[0])
        reach=int(newl[2])
        pixelmap=[]
        temp=[]
        cnt=0
        for x in range(len(finall)):
            temp.append(finall[x])
            cnt+=1
            if cnt==numcols:
                pixelmap.append(temp)
                temp=[]
                cnt=0
        #blur the pixels 
        pixelmap=blur.averagePixels(pixelmap,numrows,numcols,reach)
        #print it out 
        blur.writeOut(lines,pixelmap)
    except IOError:
        print("Unable to open "+newl[1])
        quit
