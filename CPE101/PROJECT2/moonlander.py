# Project 2 - moonlander
#
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9
import landerFuncs

def main():
#initialize variables
   time=0
   velocity=0
   rate=0
#begin simulator
   landerFuncs.showWelcome()
   altitude = landerFuncs.getAltitude()
   fuel=landerFuncs.getFuel()
   print('')
   print('LM state at retrorocket cutoff')
#Update the LM based on the altitude 
   while altitude>0:
#determine weather or not to keep printing the state of the LM
      if fuel>0:
         landerFuncs.displayLMState(time, altitude, velocity, fuel, rate)
         rate=landerFuncs.getFuelRate(fuel)
         fuel=landerFuncs.updateFuel(fuel,rate)
#if the LM is out of fuel this will display the error 
      else:
         print('OUT OF FUEL - Elapsed Time:%4d Altitude:%8.2f Velocity:%8.2f'%(time,altitude,velocity))
         rate=0
#even with the error the variables must still be updated 
      acceleration=landerFuncs.updateAcceleration(1.62,rate)
      altitude=landerFuncs.updateAltitude(altitude,velocity,acceleration)
      velocity=landerFuncs.updateVelocity(velocity,acceleration)
      time=time+1
#makes it so that if the altitutde is negative it will print it as 0 
   if altitude<0:
      altitude=0
#display the final LM state
   landerFuncs.displayLMState(time, altitude, velocity, fuel, rate)
   landerFuncs.displayLMLandingStatus(velocity)
   
 

if __name__ == '__main__':
   main()
