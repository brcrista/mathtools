import unittest
from sum_square_difference import solution

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(10), 2640)
        self.assertEqual(solution(100), 25164150)

if __name__ == '__main__':
    unittest.main()
