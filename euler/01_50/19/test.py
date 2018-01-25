import unittest
from solution import count_sundays_on_first_of_month

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(count_sundays_on_first_of_month(), 171)

if __name__ == '__main__':
    unittest.main()
