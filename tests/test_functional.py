from string import ascii_lowercase
from mathtools.functional import argmax, argmin, identity

def test_argmax() -> None:
    assert argmax(identity, ascii_lowercase) == 'z'
    assert argmax(lambda x: x * x, range(-5, 6)) == -5

def test_argmin() -> None:
    assert argmin(identity, ascii_lowercase) == 'a'
    assert argmin(lambda x: x * x, range(-5, 6)) == 0
