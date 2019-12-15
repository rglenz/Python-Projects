#Raymond Lenz
#Sussan Einakian 
#Section 9 
#Lab 8

#This function will create a list of the lines in in.txt
# ->list
def createList():
    f=open('in.txt')
    lines=f.readlines()
    for x in range(len(lines)):
        lines[x]=lines[x].strip()
    lines.pop()
    return(lines)
#This function will count the amount of characters in each line and print it in the correct format
#list->
def charcnt(l):
    for x in range(len(l)):
        cnt=0
        for y in l[x]:
            cnt+=1
        print('Line',x,'('+str(cnt)+' chars):',l[x])
l=createList()
charcnt(l)
