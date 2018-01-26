"""
Do discrete math in Python.
"""

from functools import reduce
from operator import mul
from typing import overload, Any, Iterator

__all__ = [
    "combinatorics",
    "functional",
    "number_theory"
]

#pylint: disable=unused-argument,function-redefined
@overload
def product(xs: Iterator[int]) -> int:
    pass

@overload
def product(xs: Iterator[float]) -> float:
    pass

def product(xs):
    """The product of all numbers in an `Iterator`."""
    return reduce(mul, xs, 1)
#pylint: enable=unused-argument,function-redefined
