import unittest
from solution import large_sum

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(large_sum(), '5537376230')

if __name__ == '__main__':
    unittest.main()
