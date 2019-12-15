#Raymond Lenz
#Sussan Einakian
#Section 9
#Lab 8
import objects as o
import funcs_objects as f
#This function will take in a list of Point Objects and return a list that determines the distances from the point to the origin
#list -> list
def distance_all(l):
    l2=list(map(lambda x:f.distance(o.Point(0,0),x),l))
    return(l2)
#This function will take in a list of Point Objects and return a list that determines if the point is in the first quadrant
#list -> list
def are_in_first_quadrant(l):
    l2=list(filter(lambda p: p.x>0 and p.y>0,l))
    return(l2)

