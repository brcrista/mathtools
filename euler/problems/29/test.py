import unittest
from solution import distinct_powers

class Test(unittest.TestCase):
    def test_distinct_powers(self):
        self.assertEqual(distinct_powers(5), 15)
        self.assertEqual(distinct_powers(100), 9183)

if __name__ == '__main__':
    unittest.main()
