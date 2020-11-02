import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyStringMultiplicationTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_stringmultiplication(self):
        test_data = CsvReader('/src/Unit Test string-multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.stringmultiply(row['Value 1'], row['Value 2']), (row['Result']))
            self.assertEqual(self.calculator.result, (row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()