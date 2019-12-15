import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_bitwise(self):
        self.assertAlmostEqual(bitwise_shift(4,2,'>>'), 1)
        self.assertAlmostEqual(bitwise_shift(4,2,'<<'), 16)
        self.assertAlmostEqual(bitwise_shift(100,50,'<<'), 112589990684262400)
        self.assertAlmostEqual(bitwise_shift(27,5,'<<'), 864)
    def test_infix_to_postfix_prec(self):
        self.assertAlmostEqual(infix_to_postfix_prec("<<"), ("<<",3))
        self.assertAlmostEqual(infix_to_postfix_prec(">>"), (">>",3))
        self.assertAlmostEqual(infix_to_postfix_prec("*"),("*", 1))
        self.assertAlmostEqual(infix_to_postfix_prec("/"), ("/",1))
        self.assertAlmostEqual(infix_to_postfix_prec("**"),("**",2))
        self.assertAlmostEqual(infix_to_postfix_prec("+"), ("+",0))
        self.assertAlmostEqual(infix_to_postfix_prec("-"), ("-",0))
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("360"), 360)
        self.assertAlmostEqual(postfix_eval("360.2"), 360.2)
        self.assertAlmostEqual(postfix_eval("360.0"), 360.0)
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        self.assertAlmostEqual(postfix_eval("3.6 5.3 +"), 8.9)
        self.assertAlmostEqual(postfix_eval("3.6 5.3 *"), 19.08)
        self.assertAlmostEqual(postfix_eval("3.6 5.3 /"), 0.67924528301)
        self.assertAlmostEqual(postfix_eval("3.6 5.3 **"), 887.9801427276378)
        self.assertAlmostEqual(postfix_eval("3.6 5.3 -"), -1.7)
        self.assertAlmostEqual(postfix_eval("3.0 5.0 +"), 8)
        self.assertAlmostEqual(postfix_eval("4.0 8.0 2.0 / **"), 256)
        self.assertAlmostEqual(postfix_eval("4 8 2 / **"), 256)
        self.assertAlmostEqual(postfix_eval("5 3 2 * 8 + *"), 70)
        self.assertAlmostEqual(postfix_eval("4 5 7 2 + - *"),-16)
        self.assertAlmostEqual(postfix_eval("-4 5 7 2 + - *"),16)
        self.assertAlmostEqual(postfix_eval("2 3 2 ** **"),512)
        self.assertAlmostEqual(postfix_eval("2 3 >> 1 +"),1)
        self.assertAlmostEqual(postfix_eval("2 3 << 2 *"),32)
    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        
    def test_postfix_eval_03(self):
        with self.assertRaises(ValueError):  # used to check for exception
            postfix_eval("2 0 /")
    def test_postfix_eval_04(self):
        try:
            postfix_eval("0 2 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("0 2 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("3 3 / 1 <<")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("2.0 3 << 2 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("2 3.0 << 2 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("2.0 3 >> 2 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        try:
            postfix_eval("2 3.0 >> 2 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")
        
    def test_postfix_eval_05(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_infix_to_postfix_01(self):
        self.assertEqual("2 3 4 5 / / /", infix_to_postfix("2 / ( 3 / ( 4 / 5 ) )"))
        self.assertEqual("5 6 3 + 7 3 * - 2 + * 6 /", infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"))
        self.assertEqual(infix_to_postfix("6.1 - 3.3"), "6.1 3.3 -")
        self.assertEqual(infix_to_postfix("( ( 6.1 - 3.3 ) * 9 ) / 2"), "6.1 3.3 - 9 * 2 /")
        self.assertEqual(infix_to_postfix("( ( 6.1 - 3.3 + 4 ) * 9 ) / 2"), "6.1 3.3 - 4 + 9 * 2 /")
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("21.0"), "21.0")
        self.assertEqual(infix_to_postfix("6.0 - 3.0"), "6.0 3.0 -")
        self.assertEqual(infix_to_postfix("6 - 3 * 3"), "6 3 3 * -")
        self.assertEqual(infix_to_postfix("-6 - -3 * -3"), "-6 -3 -3 * -")
        self.assertEqual(infix_to_postfix("6 - 3 << 4"), "6 3 4 << -")
        self.assertEqual(infix_to_postfix("( 6 - 3 ) + ( 3 << 4 )"), "6 3 - 3 4 << +")
        self.assertEqual(infix_to_postfix("( 6 - 3 ) + ( 3 >> 4 ** 3 )"), "6 3 - 3 4 >> 3 ** +")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("( ( ( 6 * 4 / 3 ) * 2 ) + ( 2 + 1 ) )"), "6 4 * 3 / 2 * 2 1 + +")
        self.assertEqual(infix_to_postfix("( ( ( 6 * 4 ** 3 ) * 2 ) + ( 2 + 1 ) )"), "6 4 3 ** * 2 * 2 1 + +")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("6 ** 3 ** 4 ** 5"), "6 3 4 5 ** ** **")
        self.assertEqual(infix_to_postfix("6 + 3 + 4 + 5"), "6 3 + 4 + 5 +")
        self.assertEqual(infix_to_postfix("-6 + -3 + -4 + -5"), "-6 -3 + -4 + -5 +")
        self.assertEqual(infix_to_postfix("2 ** 3 ** 2"),"2 3 2 ** **")
        self.assertEqual(infix_to_postfix("1 >> 3 ** 2"),"1 3 >> 2 **")
        self.assertEqual(infix_to_postfix("10 >> 31 ** 267"),"10 31 >> 267 **")

        
    def test_prefix_to_postfix_02(self):
        self.assertEqual(prefix_to_postfix("35"), "35")
        self.assertEqual(prefix_to_postfix("35.0"), "35.0")
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* - 3.0 / 2.0 1.0 - / 4.0 5.0 6.0"), "3.0 2.0 1.0 / - 4.0 5.0 / 6.0 - *")
        self.assertEqual(prefix_to_postfix("* - 30 / 245 19 - / 4 5 6"), "30 245 19 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("* - -30 / -245 -19 - / 4 5 6"), "-30 -245 -19 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("+ 1 * 2 3"),"1 2 3 * +")
        self.assertEqual(prefix_to_postfix("+ 1.3 * 2.5 3.8"),"1.3 2.5 3.8 * +")
        self.assertEqual(prefix_to_postfix("+ 1 << 2 3"),"1 2 3 << +")
        self.assertEqual(prefix_to_postfix(">> 1 * 2 3"),"1 2 3 * >>")
        self.assertEqual(prefix_to_postfix("** 2 + 2 3"),"2 2 3 + **")
if __name__ == "__main__":
    unittest.main()
