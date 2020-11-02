import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MySquarerootTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_squareroot(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertAlmostEqual(self.calculator.sqrt(row['Value 1']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()