import unittest
from solution import lattice_paths

class Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(lattice_paths(), 137846528820)

if __name__ == '__main__':
    unittest.main()
