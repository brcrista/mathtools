import unittest
from smallest_multiple import solution

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(10), 2520)
        self.assertEqual(solution(20), 232792560)

if __name__ == '__main__':
    unittest.main()
