from simple_calculator import SimpleCalculator
import unittest 
Class TestSimpleCalculator(unittest.TestCase):
def setUp(self):
    self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        def test_subtraction(self):
            self.assertEqual(self.calc.subtract(5, 3), 2)
            self.assertEqual(self.calc.subtract(0,0), 0)
            self.assertEqual(self.cal.subtract(-5, -3), -2)
            self.assertEqual(self.calc.subtract(3, 5), -2)
            self.assrtEqual(self.calc.subtract(-3, 5), -8)
        def test_multiplication(self):
                             self.assertEqual(self.calc.multiply(2,3),6)
                             self.asseertEqual(self.calc.multiply(-1, 5), -5)
                             self.assertEqual(self.calc.multiply(0, 5), 0)
                             self.assertEqual(self.calc.multiply(5, -1), -5)
        def test_division(self):
                             self.assertEqual(self.calc.divide(6,3), 2.0)
                             self.assertEqual(self.calc.divide(5, 2), 2.5)
                             self.assertEqual(self.calc.divide(5, 0), None)
                             self.assertEqual(self.calc.divide(0, 5), 0.0)
                             

                             )