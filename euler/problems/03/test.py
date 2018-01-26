import unittest
from largest_prime_factor import solution

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(13195), 29)
        self.assertEqual(solution(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()
