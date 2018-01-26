import unittest
from solution import special_pythagorean_triple

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(special_pythagorean_triple(), 31875000)

if __name__ == '__main__':
    unittest.main()
