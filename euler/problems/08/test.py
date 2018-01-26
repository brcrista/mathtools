import unittest
from solution import largest_product_in_series

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(largest_product_in_series(4), 5832)
        self.assertEqual(largest_product_in_series(13), 23514624000)

if __name__ == '__main__':
    unittest.main()
