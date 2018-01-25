import unittest
from solution import british_coins, coin_sums

class Test(unittest.TestCase):
    def test_coin_sums(self):
        self.assertEqual(coin_sums(0, [1, 2, 3]), 1)
        self.assertEqual(coin_sums(0, []), 1)
        self.assertEqual(coin_sums(100, []), 0)
        self.assertEqual(coin_sums(1, [1]), 1)
        self.assertEqual(coin_sums(2, [1]), 1)
        self.assertEqual(coin_sums(2, [2, 1]), 2)
        self.assertEqual(coin_sums(10, [2]), 1)
        self.assertEqual(coin_sums(10, [3]), 0)
        self.assertEqual(coin_sums(10, [1, 2, 5]), 10)
        self.assertEqual(coin_sums(10, [1, 2, 5, 10]), 11)
        self.assertEqual(coin_sums(200, british_coins), 73682)

if __name__ == '__main__':
    unittest.main()
