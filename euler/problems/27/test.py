import unittest
from solution import consecutive_primes, quadratic_primes

class Test(unittest.TestCase):
    def test_consecutive_primes(self):
        self.assertEqual(consecutive_primes(lambda x: (x * x) + x + 41), 40)

    def test_quadratic_primes(self):
        self.assertEqual(quadratic_primes(), -59231)

if __name__ == '__main__':
    unittest.main()
