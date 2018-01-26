import unittest
from solution import nth_lexicographic_permutation

class Test(unittest.TestCase):
    def test_nth_lexicographic_permutation(self):
        self.assertEqual(nth_lexicographic_permutation(range(0, 3), 4), 120)
        self.assertEqual(nth_lexicographic_permutation(range(0, 10), 1000000), 2783915460)

if __name__ == '__main__':
    unittest.main()
