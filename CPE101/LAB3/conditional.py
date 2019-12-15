#Lab 3 
#Raymond Lenz
#Section:9
#This function will find the max of two integers
#int int -> int
def max_101(x,y):
        if(x>y):
                return (x)
        elif(y>x):
                return (y)
#this function will find the max of three float values
#float float float -> float
def max_of_three(x,y,z):
        if(x>y and x>z):
                return(x)
        elif(y>x and y>z):
                return(y)
        elif(z>x and z>y):
                return(z)
#This function will calculate a late fee for a rental based on how many days it has been
#int->int
def rental_late_fee(x):
        if (x<=0):
                return (0)
        elif(x<=9):
	        return(5)
        elif(x<=15):
                return(7)
        elif(x<=24):
                return(19)     
        elif(x>24):
                return(100)
