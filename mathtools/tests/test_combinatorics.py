import unittest
from mathtools.combinatorics import binomial_coefficient

class Test(unittest.TestCase):
    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coefficient(1, 0), 1)
        self.assertEqual(binomial_coefficient(1, 1), 1)
        self.assertEqual(binomial_coefficient(10, 10), 1)
        self.assertEqual(binomial_coefficient(10, 1), 10)
        self.assertEqual(binomial_coefficient(4, 2), 6)

        self.assertEqual(binomial_coefficient(6, 0), 1)
        self.assertEqual(binomial_coefficient(6, 1), 6)
        self.assertEqual(binomial_coefficient(6, 2), 15)
        self.assertEqual(binomial_coefficient(6, 3), 20)
        self.assertEqual(binomial_coefficient(6, 4), 15)
        self.assertEqual(binomial_coefficient(6, 5), 6)
        self.assertEqual(binomial_coefficient(6, 6), 1)

if __name__ == '__main__':
    unittest.main()
