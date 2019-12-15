#Lab 3
#Name: Raymond Lenz
#Section: 9 
import unittest
import logic

#You can dlete pass after wrinting your code
class TestCases(unittest.TestCase):
        def test_is_even(self):
                self.assertTrue(logic.is_even(2))
                self.assertFalse(logic.is_even(3))
                self.assertFalse(logic.is_even(5))
                pass
        def test_is_an_interval(self):
                self.assertFalse(logic.is_an_interval(-10))
                self.assertTrue(logic.is_an_interval(0))
                self.assertFalse(logic.is_an_interval(9))
                self.assertTrue(logic.is_an_interval(20))
                self.assertTrue(logic.is_an_interval(122))
                self.assertTrue(logic.is_an_interval(0))
                pass


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

