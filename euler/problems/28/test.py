import unittest
from solution import sum_of_number_spiral_diagonals

class Test(unittest.TestCase):
    def test_sum_of_number_spiral_diagonals(self):
        self.assertEqual(sum_of_number_spiral_diagonals(5), 101)
        self.assertEqual(sum_of_number_spiral_diagonals(1001), 669171001)

if __name__ == '__main__':
    unittest.main()
