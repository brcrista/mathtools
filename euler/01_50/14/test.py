import unittest
from solution import collatz_sequence, longest_collatz_sequence

class Test(unittest.TestCase):
    def test_collatz_sequence(self):
        self.assertEqual(collatz_sequence(1), [1])
        self.assertEqual(collatz_sequence(13), [13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

    def test_solution(self):
        self.assertEqual(longest_collatz_sequence(1000000), 837799)

if __name__ == '__main__':
    unittest.main()
