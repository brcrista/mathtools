import doctest
import unittest
from mathtools import product
from mathtools.number_theory import *

def load_tests(loader, tests, ignore):
    import mathtools.number_theory
    tests.addTests(doctest.DocTestSuite(mathtools.number_theory))
    return tests

class Test(unittest.TestCase):
    def test_divides(self):
        self.assertTrue(divides(1, 1))
        self.assertTrue(divides(10, 5))
        self.assertFalse(divides(5, 10))
        self.assertTrue(divides(0, 2))

    def test_even_odd(self):
        evens = [-1000, -4, -2, 0, 2, 4, 1000]
        odds = [-1001, -1, 1, 5, 7, 63]
        for n in evens:
            self.assertTrue(even(n))
            self.assertFalse(odd(n))
        for n in odds:
            self.assertFalse(even(n))
            self.assertTrue(odd(n))

    def test_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 41]
        composites = [4, 6, 12, 100, 10000]
        for n in primes:
            self.assertTrue(is_prime(n))
        for n in composites:
            self.assertFalse(is_prime(n))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))

    def test_factors(self):
        self.assertRaises(ValueError, lambda: factors(0))
        self.assertEqual(factors(1), [1])
        self.assertEqual(factors(2), [1, 2])
        self.assertEqual(factors(8), [1, 2, 4, 8])

    def test_prime_factorization(self):
        self.assertRaises(ValueError, lambda: prime_factorization(0))
        self.assertEqual(prime_factorization(24), [2, 2, 2, 3])
        self.assertEqual(prime_factorization(42), [2, 3, 7])
        self.assertEqual(prime_factorization(100), [2, 2, 5, 5])
        self.assertEqual(prime_factorization(47231016), [2, 2, 2, 3, 7, 41, 6857])

    def test_product(self):
        self.assertEqual(product([]), 1)
        self.assertEqual(product([1, 2, 3]), 6)
        self.assertEqual(product(range(0, 10000)), 0)

    def test_lcm(self):
        self.assertEqual(lcm(0, 100), 0)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(1, 123456), 123456)
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(6, 4), 12)

if __name__ == '__main__':
    unittest.main()
