import unittest
from solution import is_abundant, lower_limit_of_abundant_sums, non_abundant_sums

abundants_less_than_100 = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96]

class Test(unittest.TestCase):
    def test_is_abundant(self):
        self.assertFalse(any(is_abundant(i) for i in range(1, 12)))
        self.assertTrue(all(is_abundant(i) for i in abundants_less_than_100))

    def test_non_abundant_sums(self):
        self.assertEqual(non_abundant_sums(12), sum(range(1, 12)))
        self.assertEqual(non_abundant_sums(lower_limit_of_abundant_sums), 4179871)

if __name__ == '__main__':
    unittest.main()
