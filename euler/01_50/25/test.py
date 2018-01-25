import unittest
from solution import index_of_first_thousand_digit_fibonacci_number

class Test(unittest.TestCase):
    def test_index_of_first_thousand_digit_fibonacci_number(self):
        self.assertEqual(index_of_first_thousand_digit_fibonacci_number(), 4782)

if __name__ == '__main__':
    unittest.main()
