# Project 1 
# 
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9

import funcs

velocityObject=0
velocitySkater=0
massObject=0.0
massSkater=0
distance=0
pounds=0
obj=''
def main():
#this section of the code will take in all the user inputs and save them to varialbes so they can be used in the functions 
        print('How much do you weigh(pounds)? ')
        pounds=int(input())
        print('How far away is your professor(meters)? ')
        distance= int(input())
        print('Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ightsaber, or lawn (g)nome? ')
        obj= input()
#This section of the code calls the getMassObject function and then runs a conditional statement to see what to print as a comment on the professor's health based on the objects mass
        massObject=(funcs.getMassObject(obj))
        if (massObject<=.1):
                print('Nice throw! Youre going to get an F!')
        elif(.1<massObject<=1.0):
                print('Nice throw! Make sure your professor is OK.')
        elif(1.0<massObject):
                if(distance<20):
                        print('Nice throw! How far away is the Hospital?')
                else:
                        print('Nice throw! RIP professor.')
#this section calls all the functions in order to obtain the values to find the skaters velocity 
        velocityObject=(funcs.getVelocityObject(distance))
        massSkater=(funcs.poundsToKG(pounds))
        velocitySkater=(funcs.getVelocitySkater(massSkater,massObject,velocityObject))
#Using %f I have formatted the output to have three decimal places 
        print ('Velocity of skater:', '%.3f'%velocitySkater,'m/s')
#This section of the code determines if it should print another comment about the skaters velocity 
        if(velocitySkater<0.2):
                print('My grandmother skates faster than you!')
        elif(.2<=velocitySkater<1.0):
                print('')
        else:
                print('Look out for that railing!!!')
if __name__ == '__main__':
        main()

