#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9

#This function takes in a list of numbers and makes them into a nested list with three elements in each. If the amount of elements isn't divisible by three then it will fill it partially 
#list -> list
def groups_of_3(l):
    finall=[]
    linl=[]
    cnt=0
    for x in range(len(l)):
        linl.append(l[x])
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

        

