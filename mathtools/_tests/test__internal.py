import unittest
from mathtools._internal import *

class Test(unittest.TestCase):
        self.assertFalse(is_iterable(1))
        self.assertTrue(is_iterable([]))

if __name__ == '__main__':
    unittest.main()
