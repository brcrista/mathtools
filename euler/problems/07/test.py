import unittest
from solution import nth_prime

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(nth_prime(6), 13)
        self.assertEqual(nth_prime(10001), 104743)

if __name__ == '__main__':
    unittest.main()
