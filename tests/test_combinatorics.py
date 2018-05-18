from mathtools.iterator import take
from mathtools.combinatorics import binomial_coefficient, recurrence

def test_recurrence() -> None:
    it = recurrence([], lambda: 100)
    assert take(3, it) == [100, 100, 100]

    it = recurrence([1], lambda x: x + 1)
    assert take(5, it) == [1, 2, 3, 4, 5]

    it = recurrence(['a', 'b', 'c'], lambda x, y, z: x + y + z)
    assert take(5, it) == ['a', 'b', 'c', 'abc', 'bcabc']

def test_binomial_coefficient() -> None:
    assert binomial_coefficient(1, 0) == 1
    assert binomial_coefficient(1, 1) == 1
    assert binomial_coefficient(10, 10) == 1
    assert binomial_coefficient(10, 1) == 10
    assert binomial_coefficient(4, 2) == 6

    assert binomial_coefficient(6, 0) == 1
    assert binomial_coefficient(6, 1) == 6
    assert binomial_coefficient(6, 2) == 15
    assert binomial_coefficient(6, 3) == 20
    assert binomial_coefficient(6, 4) == 15
    assert binomial_coefficient(6, 5) == 6
    assert binomial_coefficient(6, 6) == 1
