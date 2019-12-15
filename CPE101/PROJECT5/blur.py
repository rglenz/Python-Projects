#Project 5
#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9
#
#
#
#PSEUDOCODE:
#I am going to create 3 functions to complete the blur.
#First will be the createList function which will take in the lines of the ppm file and return a list of all the pixels.
#The next function will average all the pixels that are in the reach of the current pixel which will create the blur effect.
#I will use a double for loop and add all of the red, green, and blue values of each pixel that is in the reach and finally divide by the number of pixels used.
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
#This function averages all of the pixels based on the reach to create the blur
#list int int int -> list
def averagePixels(pixellist,numrows,numcols,reach):
    finalPixels=[]
    cnt=0
    r=0
    g=0
    b=0      
    for row in range(numrows):
        for col in range(numcols):
            for x in range(-reach,reach+1):
                if row+x>numrows-1:
                    continue
                if col+x>numcols-1:
                    continue
                if row+x<0:
                    continue
                if col+x<0:
                    continue
                cnt+=1
                r+=int(pixellist[row+x][col][0])
                g+=int(pixellist[row+x][col][1])
                b+=int(pixellist[row+x][col][2])
            for x in range(-reach,reach+1):
                if row+x>numrows-1:
                    continue
                if col+x>numcols-1:
                    continue
                if row+x<0:
                    continue
                if col+x<0:
                    continue
                cnt+=1
                r+=int(pixellist[row][col+x][0])
                g+=int(pixellist[row][col+x][1])
                b+=int(pixellist[row][col+x][2])
            
            finalPixels.append([int(r/cnt),int(g/cnt),int(b/cnt)])
            cnt=0
            r=0
            g=0
            b=0    
    return(finalPixels)  
#This file will write the output to a PPM file 
#list list->      
def writeOut(lines,finall):
    fout=open('blur.ppm','w')
    fout.write(str(lines[0]))
    fout.write(str(lines[1]))
    fout.write(str(lines[2]))
    for x in finall:
        for y in x:
            fout.write(str(y)+'\n')
