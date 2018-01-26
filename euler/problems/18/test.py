import unittest

from core import parse_grid
from solution import longest_path, TRIANGLE

TEST_INPUT_1 = """
3
7 4
2 4 6
8 5 9 3
"""

class Test(unittest.TestCase):
    def test_longest_path(self):
        self.assertEqual(longest_path([[1]]), 1)

    def test_solution(self):
        self.assertEqual(longest_path(parse_grid(TEST_INPUT_1)), 23)
        self.assertEqual(longest_path(parse_grid(TRIANGLE)), 1074)

if __name__ == '__main__':
    unittest.main()
