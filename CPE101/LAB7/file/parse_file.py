#Raymond Lenz
#Instructor: Sussan Einakian
#Section: 9
import sys 
newl=sys.argv
#determine if the command line arguments are correct 
if len(newl)==2:
   pass
if len(newl)<=1 or len(newl)>3:
   print('Usage:[-s]file_name')
   exit()
#Exceptions
try: 
   fileidx=1
   if '-s' in newl:
      modidx=newl.index('-s')
      if fileidx==modidx:
         fileidx=2
   fin=open(newl[fileidx])
   o=0
   f=0
   i=0
   s=0
   for line in fin:
      l=line.split()
      for item in l:
         if item.isdigit():
            i+=1
            s+=int(item)
         else:
            try:
               type(float(item))==float
            except:
               o+=1
               continue
            f+=1
            s+=float(item)
   print('Ints:',i)
   print('Floats:',f)
   print('Other:',o)
   if "-s" in newl:
      print('Sum:',s)
except Exception:
   print('Unable to open',newl[fileidx])


      

