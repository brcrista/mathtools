import unittest
from mathtools.functional import *

class Test(unittest.TestCase):
    def test_argmax(self):
        self.assertEqual(argmax(lambda x: x, [0, 1, 5, 3]), 5)
        self.assertEqual(argmax(lambda x, y: x + y, [(0, 1), (1, 5), (3, 2)]), (1, 5))
        self.assertEqual(argmax(lambda x: x, ascii_lowercase), 'z')
        self.assertEqual(argmax(lambda x: x * x, range(-5, 6)), -5)

if __name__ == '__main__':
    unittest.main()
