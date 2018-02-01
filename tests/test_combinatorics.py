from mathtools.combinatorics import binomial_coefficient

def test_binomial_coefficient():
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
