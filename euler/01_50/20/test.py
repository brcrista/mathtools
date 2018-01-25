import unittest
from solution import factorial_digit_sum

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(factorial_digit_sum(10), 27)
        self.assertEqual(factorial_digit_sum(100), 648)

if __name__ == '__main__':
    unittest.main()
