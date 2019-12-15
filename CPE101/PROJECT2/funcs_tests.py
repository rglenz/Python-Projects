#at least 3 test cases for each function
#Project 2
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9
import unittest
import landerFuncs

class TestCases(unittest.TestCase):
   #first test for updateAcceleration
   def test_updateAcceleration_1(self):
      self.assertAlmostEqual(landerFuncs.updateAcceleration(10,5),0)
      self.assertAlmostEqual(landerFuncs.updateAcceleration(20,10),20)
      self.assertAlmostEqual(landerFuncs.updateAcceleration(50,15),100)
 #tests updateAltitutde
   def test_updateAltitude_1(self):
      self.assertAlmostEqual(landerFuncs.updateAltitude(100,10,10),115)
      self.assertAlmostEqual(landerFuncs.updateAltitude(1000,10,100),1060)
      self.assertAlmostEqual(landerFuncs.updateAltitude(256,64,20),330)
  #tests updateVelocity
   def test_updateVelocity_1(self):
      self.assertAlmostEqual(landerFuncs.updateVelocity(100,10),110)
      self.assertAlmostEqual(landerFuncs.updateVelocity(12,13),25)
      self.assertAlmostEqual(landerFuncs.updateVelocity(50,6),56)
   #tests updateFuel
   def test_updateFuel_1(self):
      self.assertAlmostEqual(landerFuncs.updateFuel(100,10),90)
      self.assertAlmostEqual(landerFuncs.updateFuel(62,32),30)
      self.assertAlmostEqual(landerFuncs.updateFuel(10,20),-10)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

