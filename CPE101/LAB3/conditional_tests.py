#Lab 3
#Name: Raymond Lenz
#Section: 9 
import unittest
import conditional

class TestCases(unittest.TestCase):

   def test_max_101(self):
      self.assertTrue(conditional.max_101(10,9),10)
      self.assertTrue(conditional.max_101(10,7),10)
      self.assertTrue(conditional.max_101(1,9),9)
      pass

   def test_max_of_three(self):
      self.assertTrue(conditional.max_of_three(11,10,9),11)
      self.assertTrue(conditional.max_of_three(30,33,25),33)
      self.assertTrue(conditional.max_of_three(1,6.9,100.2),100.2)
      pass

   def test_rental_late_fee(self):
      self.assertEqual(conditional.rental_late_fee(8),5)
      self.assertEqual(conditional.rental_late_fee(25),100)
      self.assertEqual(conditional.rental_late_fee(0),0)
      self.assertEqual(conditional.rental_late_fee(14),7)
      self.assertEqual(conditional.rental_late_fee(23),19)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

