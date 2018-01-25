import unittest
from solution import largest_product_in_grid, parse_grid, GRID

DOWN = [
    list(range(0, 5)),
    list(range(0, 5)),
    list(range(0, 5)),
    list(range(0, 5))
]

RIGHT_DIAGONAL = [
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2]
]

class Test(unittest.TestCase):
    def test_largest_product_in_grid(self):
        self.assertEqual(largest_product_in_grid(DOWN), 4 ** 4)
        self.assertEqual(largest_product_in_grid(RIGHT_DIAGONAL), 16)

    def test_solution(self):
        self.assertEqual(largest_product_in_grid(parse_grid(GRID)), 70600674)

if __name__ == '__main__':
    unittest.main()
