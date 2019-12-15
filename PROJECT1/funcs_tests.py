# Project 1 
# 
# Name: Raymond Lenz
# Instructor: S. Einakian 
# Section: 9

import unittest
import funcs
class TestCases(unittest.TestCase):
        def test_poundsToKG(self):
                self.assertAlmostEqual(funcs.poundsToKG(100),45.3592)
                self.assertAlmostEqual(funcs.poundsToKG(146),66.224432)
        def test_getMassObject(self):
                self.assertEqual(funcs.getMassObject('g'),5.3)
                self.assertEqual(funcs.getMassObject('l'),9.07)
                self.assertEqual(funcs.getMassObject('t'),.1)
                self.assertEqual(funcs.getMassObject('p'),1.0)
                self.assertEqual(funcs.getMassObject('r'),3.0)
                self.assertEqual(funcs.getMassObject('4'),0)
        def test_getVelocityObject(self):
                self.assertAlmostEqual(funcs.getVelocityObject(50),15.6524758425)
                self.assertAlmostEqual(funcs.getVelocityObject(126),24.847535089)
        def test_getVelocitySkater(self):
                self.assertAlmostEqual(funcs.getVelocitySkater(100,3.0,20),.6)
                self.assertAlmostEqual(funcs.getVelocitySkater(200,5.0,100),2.5)
      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

