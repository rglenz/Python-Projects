#Lab 6
#Raymond Lenz 
#Instructor: Sussan Einakian 
#Section: 9
import unittest
import string_101

class TestString(unittest.TestCase):
   def test_str_rot_13(self):
      self.assertEqual(string_101.str_rot_13('HI my Name is Ray'),'UV zl Anzr vf Enl')
      self.assertEqual(string_101.str_rot_13('yo this is a test'),'lb guvf vf n grfg')
      self.assertEqual(string_101.str_rot_13('HELLO WELCOME TO THE TEST'),'URYYB JRYPBZR GB GUR GRFG')
      pass
   def test_str_translate(self):
      self.assertEqual(string_101.str_translate_101('abcdcba','a','x'),'xbcdcbx')
      self.assertEqual(string_101.str_translate_101('hi my name is ray','i','j'),'hj my name js ray')
      self.assertEqual(string_101.str_translate_101('boy if you dont','o','x'),'bxy if yxu dxnt')
      pass


if __name__ == '__main__':
   unittest.main()

