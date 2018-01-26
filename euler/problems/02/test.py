import unittest
from even_fibonacci_numbers import solution

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(4000000), 4613732)

if __name__ == '__main__':
    unittest.main()
