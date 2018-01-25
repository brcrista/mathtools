import unittest
from solution import power_digit_sum

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(power_digit_sum(15), 26)
        self.assertEqual(power_digit_sum(1000), 1366)

if __name__ == '__main__':
    unittest.main()
