#Raymond Lenz 
#Sussan Einakian 
#Section 9
#Project 6 
#
#Takes 4 Minutes to Run
#
#PSUEDOCODE: create a class called crime that takes two arguments of id, day,
# month, hour, and category. Create and eq and repr method. Every value must 
#be seperated by a tab. Create a set_time method that takes in 3 parameters,
# day month and hour. Next I will implement the Binary Search function given to us
#so that I can use it later. The next function will be create crimes that will create
#a list of crime ids that are robberies. Next sort_crimes will sort thea list by the ID number.
#Update Crimes will create crime objects with the id's that are from robberies matched uo with
#the times with the same ID using the binary search. Lastly find crimes will print out the 
#statistics involving all of the robberies from the list. Then I will create a main function
#that will implement all of these functions.
#
#
#

#this class is the crime class that will create an object for every line of
# the file.
class Crime():
    def __init__(self,iden,cat,day,month,hour):
        self.iden=iden
        self.cat=cat
        self.day=None
        self.month=None
        self.hour=None
    def __eq__(self,other):
        return int(self.iden)==int(other.iden)
    def __gt__(self,other):
        return int(self.iden)>int(other.iden)
    def __lt__(self,other):
        return int(self.iden)<int(other.iden)
    def __repr__(self):
        return('{}\t{}\t{}\t{}\t{}'.format(self.iden,self.cat,self.day,self.month,self.hour)) 
    def set_time(self,day,month,hour):
        self.day=day
        self.month=int(month[0:2])
        self.hour=int(hour[0:2])%12,int(hour[0:2])//12

#This fucntion will do a binary search through a sorted list and check if an item is in it 
#list string -> Bool
def binarySearch(alist,item):
    first=0
    last=len(alist)-1
    found=False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
        else:
            if item< alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    return found
#This function will take in the crimes and create a list of id's that are a robbery
#list-> list
def create_crimes(lines):
    crimel=[]
    objl=[]
    idl=[]
    temp=[]
    for crime in lines:
        temp=[]
        temp=crime.split() 
        crimel.append(temp)
#Turn the list of info into a list of objects
    for crime in crimel:
        if crime[1]=="ROBBERY":
            c=0
            col=[]
            c=Crime(crime[0],crime[1],0,0,0)
            col=c.iden  
            if col not in objl:
                objl.append(col)
    return(objl)
#This function will sort the crimes by ID number
#list->list
def sort_crimes(crimes):
    sortl=sorted(crimes,key=lambda x: x[0])    
    return sortl
#This function will update the crimes and add their time attributes 
#list list->list
def update_crimes(crimes,lines):
    newl=[]
    cnt=0 
    finall=[]
    for line in lines:        
        if binarySearch(crimes,line[0])==True:    
            newl.append(line)
    
    for crimeid in crimes:
        for time in lines:              
            if crimeid==time[0]:           
                c=Crime(crimeid,'ROBBERY',0,0,0)
                c.set_time(time[1],time[2],time[3])
                if c not in finall:  
                    finall.append(c)
    return(finall)

#this function will print all of the info about the robberies 
#list-> 
def find_crimes(crimes):
#Find the day with the most robberies 
    l=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    dcnt=0
    nday=''
    cnt=0
    for day in l:
        cnt=0
        for crime in crimes:
            if crime.day==day:
                cnt+=1
        if cnt>dcnt:
            dcnt=cnt
            nday=day
#Find Month with the most Robberies 
    ml=[1,2,3,4,5,6,7,8,9,10,11,12]
    monthcnt=0
    maxmonth=0
    months=0
    for month in ml:
        monthcnt=0
        for crime in crimes:
            if crime.month==month:
                monthcnt+=1
        if monthcnt>maxmonth:
            maxmonth=monthcnt
            months=month
#Find the time with the most robberies 
    timel=[(1,1),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1),(11,1),(0,1),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(0,0)]
    timecnt=0
    maxtime=0
    times=0
    for time in timel:
        timecnt=0
        for crime in crimes:
            if crime.hour==time:
                timecnt+=1
            if timecnt>maxtime:
                maxtime=timecnt
                times=time
    finalmonth=['January','February','March','April','May','June','July','August','September','October','November','December']
    finalhour=['1PM','2PM','3PM','4PM','5PM','6PM','7PM','8PM','9PM','10PM','11PM','12PM','1AM','2AM','3AM','4AM','5AM','6AM','7AM','8AM','9AM','10AM','11AM','12AM']
    hidx=timel.index(times)
    midx=ml.index(months)
#Output 
    print("NUMBER OF PROCESSED ROBBERIES:",len(crimes))
    print("DAY WITH MOST ROBBERIES:",nday)
    print("MONTH WITH MOST ROBBRIES:",finalmonth[midx])
    print("HOUR WITH THE MOST ROBBERIES:",finalhour[hidx])
#Main Function
def main():
    try:
        crimeInfo=open('crimes.tsv')
        timeInfo=open('times.tsv')
    except IOError:
        print("File does not exist")
    #Create two lists, one for the times and one for the crimes 
    lines=crimeInfo.readlines()
    loc=[] 
    for x in range(len(lines)):
        loc.append(lines[x].split())
    timelines=timeInfo.readlines()
    lot=[]
    for x in range(len(timelines)):    
        lot.append(timelines[x].split())
#call all of the functions to get the answer 
    crimes=create_crimes(lines)
    sortedcrimes=sort_crimes(crimes)
    lot=sort_crimes(lot)
    updatedcrimes=update_crimes(sortedcrimes,lot)
    find_crimes(updatedcrimes)
if __name__=="__main__":
    main()
