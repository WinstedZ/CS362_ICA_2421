import calculator
import unittest

print("This is a testing program that will test the functionality of calculator.py\n"
      "Errors will be printed as they happen, so a test succeeds if no errors are printed\n\n")

class TestCase(unittest.TestCase):
      def testadd(self):
            a = 30.1
            b = 20.5
            self.assertEqual(calculator.Calc_add(a,b),50.6)

      def testsub(self):
            a = 6
            b = -3
            self.assertEqual(calculator.Calc_sub(a,b),9)
            self.assertEqual(calculator.Calc_sub(b,a),-9)

      def testmul(self):
            a = 2
            b = 4
            self.assertEqual(calculator.Calc_mul(a,b),8)

      def testdiv(self):
            a = 10
            b = 5
            self.assertEqual(calculator.Calc_div(a,b),2)
            self.assertEqual(calculator.Calc_div(b,a),0.5)

      def testdiv0(self):
            a=0
            b=2
            self.assertEqual(calculator.Calc_div(a,b),0)
            self.assertEqual(calculator.Calc_div(b,a),0)

if __name__ == '__main__':
      unittest.main(verbosity=2)