
# Project 2 - Moonlander Functions
#
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9

#This function will show the greeting text and will prompt the user with all the information they need 
# None -> None
def showWelcome():
   print('')
   print('Welcome aboard the Lunar Module Flight Simulator')
   print('')
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level.  To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print("")
   print("   Good luck and may the force be with you!")
   print('')
#This function prompts the user for an input for the amount of fuel the LM has
#None -> int 
def getFuel():
   fuel= int(input('Enter the initial amount of fuel on board the LM (in liters): '))
   while fuel<=0:
      print ("ERROR: Amount of fuel must be positive, please try again")
      fuel=int(input("Enter the initial amount of fuel on board the LM (in liters): "))
   return (fuel)
#this function prompts the user for an input that describes the current altitude of the LM
#None -> int
def getAltitude():
   altitude= int(input('Enter the initial altitude of the LM (in meters): '))
   while altitude<1 or altitude>9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      altitude= int(input("Enter the initial altitude of the LM (in meters): "))
   return (altitude)
#This function will display the state of the LM an will show the current elapsed time, altitude, velocity, fuel amount, and fuel rate
#int float float int int  -> None
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
  
   if(altitude<=0):
      print('')
      print('LM state at landing/impact')
   print('Elapsed Time:','%4d'%elapsedTime,'s')
   print('%13s'%'Fuel:','%4d'%fuelAmount,'l')
   print('%13s'%'Rate:','%4d'%fuelRate,'l/s')
   print('%13s'%'Altitude:','%7.2f'%altitude,'m')
   print('%13s'%'Velocity:','%7.2f'%velocity,'m/s')
   print('')
#This function takes in the current fuel and prompts the user for a fuel rate. After this it calculates the new fuel rate.
#int -> int
def getFuelRate(currentFuel):
   fuelRate=int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   while fuelRate<0 or fuelRate>9:
      print('ERROR: Fuel rate must be between 0 and 9, inclusive')
      print("")
      fuelRate=int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if(currentFuel<fuelRate):
      fuelRate=currentFuel
   return fuelRate   
#This function updates the LM's acceleration after a given gravity and fuel rate has been applied
#float int -> float
def updateAcceleration(gravity, fuelRate):
   acceleration= gravity*((fuelRate/5)-1)
   return acceleration
#This function updates the altitude of the LM after receiving a given altitude velocity and acceleration
#float float float -> float
def updateAltitude(altitude, velocity, acceleration):
   altitudeNew=altitude+velocity+(acceleration/2)
   return altitudeNew
#This function updates the velocity of the LM by taking in the current velocity and the acceleration
#float float -> float 
def updateVelocity(velocity, acceleration):
   velocityNew=velocity+acceleration
   return velocityNew
#This function updates the amount of fuel left by taking in the amount of current fuel and subtracting the fuel rate 
#int int -> int
def updateFuel(fuelAmount, fuelRate):
   fuelNew=fuelAmount-fuelRate
   return fuelNew
#This function displays the final status of the LM when the altitude is 0 based on the velocity 
#float -> None
def displayLMLandingStatus(velocity):
   if(-1<=velocity<=0):
      print('Status at landing - The eagle has landed!')
   elif(-10<velocity<-1):
      print('Status at landing - Enjoy your oxygen while it lasts!')
   elif(velocity<=-10):
      print('Status at landing - Ouch - that hurt!')
