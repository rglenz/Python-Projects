# Project 1 
# 
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9
velocityObject=0
velocitySkater=0
massObject=0.0
massSkater=0
distance=0
pounds=0
obj=''

print('How much do you weigh(pounds)? ')
pounds=int(input())
print('How far away is your professor(meters)? ')
distance= int(input())
print('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ightsaber, or lawn (g)nome? ')
obj= input()
print('Nice throw!')       
def getVelocityObject(distance):
        velocityObject=math.sqrt((9.8*distance)/2)
        return (velocityObject)

def getVelocitySkater(massObject,velocityObject,massSkater):
        velocitySkater=(massObject*velocityObject)/massSkater
        return (velocitySkater)

def getMassObject(obj):
	if (obj=='t'):
		massObject=.1
		return massObject
	elif(obj=='p'):
		massObject=1.0
		return massObject
	elif(obj=='r'):
		massObject=3.0
		return massObject
	elif(obj=='g'):
		massObject=5.3
		return massObject
	elif(obj=='l'):
		massObject=9.07
		return massObject
	else:
		print('error selection made is not an option')
massObject=getMassObject(obj)
if (massObject<=.1):
        print('You are going to get an F!')
elif(.1<massObject<=1.0):
        print('Make sure your professor is OK.')
elif(1.0<massObject):
        if(distance<20):
                print('How far away is the Hospital?')
        else:
                print('RIP professor.')
print(getMassObject(obj))


