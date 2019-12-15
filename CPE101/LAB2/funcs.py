#Lab 2 Functions 
#Name: Raymond Lenz
#Section: 9 
import math 
#takes an x and a y and runs a mathematical function 
#int int -> float
def math_func1(x,y):
      ans=((x**3)+(y**3))/(5*x+7)
      return(ans)
#takes in three integers that are meant to be coefficients of a quadratic and it computes the quadratic formula
#int int int->float
def math_func2(a,b,c):
      ans=(-b+math.sqrt(b**2-4*a*c))/2*a
      return(ans)
#finds the distance between two points 
#int int int int->float
def math_func3(x1,x2,y1,y2):
        ans=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return(ans)
#takes in a single number and finds if it is negative or not 
#float->bool
def is_negative(x):
        return(x<0)
#Takes in a single number and finds out if it is divisible by 5 
#float->bool
def is_dividable_by_5(x):
        return(x%5==0)



