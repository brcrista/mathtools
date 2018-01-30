import doctest
import unittest
from string import ascii_lowercase
from mathtools.functional import *

def load_tests(loader, tests, ignore):
    import mathtools.functional
    tests.addTests(doctest.DocTestSuite(mathtools.functional))
    return tests

class Test(unittest.TestCase):
    def test_argmax(self):
        self.assertEqual(argmax(identity, ascii_lowercase), 'z')
        self.assertEqual(argmax(lambda x: x * x, range(-5, 6)), -5)

    def test_argmin(self):
        self.assertEqual(argmin(identity, ascii_lowercase), 'a')
        self.assertEqual(argmin(lambda x: x * x, range(-5, 6)), 0)

if __name__ == '__main__':
    unittest.main()
