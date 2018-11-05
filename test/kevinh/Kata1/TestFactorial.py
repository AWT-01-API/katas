from src.kevinh.Kata1.Factorial import Factorial
import unittest


class TestFactorial(unittest.TestCase):

    def test_check_true(self):
        factorial = Factorial()
        self.assertEqual(1, factorial.process(1))
        self.assertEqual(2, factorial.process(2))
        self.assertEqual(6, factorial.process(3))
        self.assertEqual(24, factorial.process(4))
        self.assertEqual(120, factorial.process(5))
        self.assertEqual(87178291200, factorial.process(14))


if __name__ == '__main__':
    unittest.main()
