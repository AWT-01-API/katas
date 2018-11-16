from src.kevinh.Kata3.NumberFormat import NumberFormat
import unittest


class TestFactorial(unittest.TestCase):
    def test_number_expanded_form(self):
        self.assertEqual(NumberFormat.expanded_form(2), '2')
        self.assertEqual(NumberFormat.expanded_form(12), '10 + 2')
        self.assertEqual(NumberFormat.expanded_form(42), '40 + 2')
        self.assertEqual(NumberFormat.expanded_form(70304), '70000 + 300 + 4')
        self.assertEqual(NumberFormat.expanded_form(4982342), '4000000 + 900000 + 80000 + 2000 + 300 + 40 + 2')
        self.assertEqual(NumberFormat.expanded_form(420370022), '400000000 + 20000000 + 300000 + 70000 + 20 + 2')
        self.assertEqual(NumberFormat.expanded_form(70304), '70000 + 300 + 4')
        self.assertEqual(NumberFormat.expanded_form(9000000), '9000000')
        self.assertEqual(NumberFormat.expanded_form(92093403034573), '90000000000000 + 2000000000000 + 90000000000 + 3000000000 + 400000000 + 3000000 + 30000 + 4000 + 500 + 70 + 3');
        self.assertEqual(NumberFormat.expanded_form(2096039485293), '2000000000000 + 90000000000 + 6000000000 + 30000000 + 9000000 + 400000 + 80000 + 5000 + 200 + 90 + 3');