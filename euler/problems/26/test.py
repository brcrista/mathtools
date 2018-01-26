import unittest
from fractions import Fraction
from solution import repetend, longest_reciprocal_repetend

class Test(unittest.TestCase):
    def test_repetend(self):
        self.assertEqual(repetend(Fraction(1, 1)), [])
        self.assertEqual(repetend(Fraction(1, 2)), [])
        self.assertEqual(repetend(Fraction(1, 3)), [3])
        self.assertEqual(repetend(Fraction(1, 6)), [6])
        self.assertEqual(repetend(Fraction(1, 7)), [1, 4, 2, 8, 5, 7])
        self.assertEqual(repetend(Fraction(1, 99)), [0, 1])

    def test_longest_reciprocal_repetend(self):
        self.assertEqual(longest_reciprocal_repetend(1000), 983)

if __name__ == '__main__':
    unittest.main()
