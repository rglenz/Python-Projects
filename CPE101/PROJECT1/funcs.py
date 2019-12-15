# Project 1 
# 
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9
import math
velocityObject=0
velocitySkater=0
massObject=0.0
massSkater=0
distance=0
pounds=0
obj=''
#This function will take in a user prompt and return the velocity of the object
#int->float
def getVelocityObject(distance):
        velocityObject=math.sqrt((9.8*distance)/2)
        return (velocityObject)

#This function will take in three inputs and calculate the velocity of the skater on the ice 
#float float float -> float
def getVelocitySkater(massSkater,massObject,velObject):
        velocitySkater=(massObject*velObject)/massSkater
        return (velocitySkater)

#this function will take determine what the mass of the user selected object is 
#string -> float
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
		massObject=0
		return massObject

#this function finds the user's weight in kilograms after it is given in pounds
#int -> float
def poundsToKG(pounds):
        kilograms=pounds*.453592
        return kilograms



