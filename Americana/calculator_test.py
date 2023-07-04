import unittest

from Americana.calculator import Calculator


class CalculatorTest(unittest.TestCase):

    def test_add(self):
        calculator = Calculator()
        expected = 5
        actual = calculator.add(2 , 3)
        self.assertEqual(expected, actual)
