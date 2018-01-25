import unittest
from solution import first_triangle_number_with_more_divisors_than

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(first_triangle_number_with_more_divisors_than(5), 28)
        self.assertEqual(first_triangle_number_with_more_divisors_than(500), 76576500)

if __name__ == '__main__':
    unittest.main()
