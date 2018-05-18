from math import factorial
from operator import add
from typing import Callable, Iterator, List, Optional, TypeVar

from mathtools import product

_T = TypeVar('_T')

def recurrence(start: List[_T], func: Callable[..., Optional[_T]]) -> Iterator[_T]:
    """
    Return an `Iterator` beginning with `start` where each element is created
    by applying `func` to the previous `len(start)` elements.

    `func()` should take `len(start)` parameters of type `_T`.
    Iteration stops when a `None` value is reached.

    >>> import itertools
    >>> it = recurrence([], lambda: 100)
    >>> list(itertools.islice(it, 3))
    [100, 100, 100]

    >>> list(recurrence([1], lambda x: x + 1 if x < 5 else None))
    [1, 2, 3, 4, 5]

    >>> import itertools
    >>> it = recurrence([1], lambda x: x * 2)
    >>> list(itertools.islice(it, 5))
    [1, 2, 4, 8, 16]
    """
    window = start
    yield from iter(start)

    value = func(*window)
    while value is not None:
        yield value
        window += [value]
        window = window[1:]
        value = func(*window)

def fibonacci_numbers() -> Iterator[int]:
    """
    The infinite sequence of Fibonacci numbers: 1, 2, 3, 5, 8, ...

    >>> import itertools
    >>> fib = fibonacci_numbers()
    >>> list(itertools.islice(fib, 5))
    [1, 2, 3, 5, 8]
    """
    return recurrence([1, 2], add)

def binomial_coefficient(n: int, k: int) -> int:
    """
    The binomial coefficient C(n, k).

    >>> binomial_coefficient(4, 3)
    4

    >>> binomial_coefficient(10, 6)
    210
    """
    return product((n + 1 - i) for i in range(1, k + 1)) // factorial(k)
