#Raymond Lenz
#Sussan Einakian 
#Section 9 
#Lab 8
import objects
#This function will find the distance of two points as long as they are objects of the class point
#Point Point->float
def distance(p1,p2):
    dist=((p1.x-p2.x)**2+(p1.y-p2.y)**2)**.5
    return dist
#This function takes in two circle object and find out if they overlap 
#Circle Circle->bool
def circles_overlap(c1,c2):
    co=False
    center1=c1.cpnt
    center2=c2.cpnt
    rad1=c1.rad
    rad2=c2.rad
    if distance(center1,center2)<rad1+rad2:
        co=True
    return co
