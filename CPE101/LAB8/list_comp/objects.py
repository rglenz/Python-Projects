#Raymond Lenz
#Sussan Einakian 
#Section 9 
#Lab 8

#This class will create an object that has an x and y value like a point 
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return('Point({},{})'.format(self.x,self.y))
    def __eq__(self,other):
        return(type(other)==Point and self.x==other.x and self.y==other.y) 
#This class will create and object that has a center point and a radius and will act as a cirlce 
class Circle:
    def __init__(self,cpnt,rad):
        self.cpnt=cpnt
        self.rad=rad
    def __repr__(self):
        return('Circle(Center Point{},Radius{})'.format(self.cpnt,self.radius))
    def __eq__(self,other):
        return(type(other)==Circle and self.cpnt==other.cpnt and self.rad==other.rad) 
    
