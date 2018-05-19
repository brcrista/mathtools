from mathtools.iterable import take, unzip

def test_take():
    assert take(0, range(0, 10)) == []
    assert take(5, [1, 2, 3]) == [1, 2, 3]
    assert take(5, (2 * i for i in range(0, 100))) == [0, 2, 4, 6, 8]

def test_unzip():
    xs = [1, 2, 3]
    ys = [4, 5, 6]
    _xs, _ys = unzip(zip(xs, ys))
    assert list(_xs) == xs
    assert list(_ys) == ys
