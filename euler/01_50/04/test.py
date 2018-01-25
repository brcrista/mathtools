import unittest
from largest_palindrome_product import solution

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(2), 9009)
        self.assertEqual(solution(3), 906609)

if __name__ == '__main__':
    unittest.main()
