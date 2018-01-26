import unittest
from solution import are_amicable, sum_of_amicable_numbers_less_than

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(sum_of_amicable_numbers_less_than(10000), 31626)

if __name__ == '__main__':
    unittest.main()
