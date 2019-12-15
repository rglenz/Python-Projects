
#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9
import unittest
import char 

class TestChar(unittest.TestCase):
   def test_is_lower_101(self):
      self.assertTrue(char.is_lower_101('a'))
      self.assertFalse(char.is_lower_101('C'))
      self.assertTrue(char.is_lower_101('z'))
      pass
   def test_char_rot13(self):
      self.assertEqual(char.char_rot13('A'),'N')
      self.assertEqual(char.char_rot13('C'),'P')
      self.assertEqual(char.char_rot13('z'),'m')
      pass


if __name__ == '__main__':
   unittest.main()

