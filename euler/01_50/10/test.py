import unittest
from solution import sum_of_primes_below

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(sum_of_primes_below(10), 17)
        self.assertEqual(sum_of_primes_below(2000000), 142913828922)

if __name__ == '__main__':
    unittest.main()
