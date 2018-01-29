from math import factorial
from typing import Callable, Iterator, Optional, TypeVar
from mathtools import product

T = TypeVar('T')

def recurrence(start: T, func: Callable[[T], Optional[T]]) -> Iterator[T]:
    """
    Return an `Iterator` beginning with `start` where each element is created
    by applying `func` to the previous element.

    Iteration stops when a `None` value is reached.

    >>> list(recurrence(None, lambda: 100))
    []

    >>> list(recurrence(1, lambda x: x + 1 if x < 5 else None))
    [1, 2, 3, 4, 5]

    >>> import itertools
    >>> it = recurrence(1, lambda x: x * 2)
    >>> list(itertools.islice(it, 5))
    [1, 2, 4, 8, 16]
    """
    current = start
    while current is not None:
        yield current
        current = func(current)

def fibonacci_numbers() -> Iterator[int]:
    """
    The infinite sequence of Fibonacci numbers: 1, 2, 3, 5, 8, ...

    >>> import itertools
    >>> fib = fibonacci_numbers()
    >>> list(itertools.islice(fib, 5))
    [1, 2, 3, 5, 8]
    """
    last1 = 1
    last2 = 0
    while True:
        fib = last1 + last2
        last2 = last1
        last1 = fib
        yield fib

def binomial_coefficient(n: int, k: int) -> int:
    """
    The binomial coefficient C(n, k).

    >>> binomial_coefficient(4, 3)
    4

    >>> binomial_coefficient(10, 6)
    210
    """
    return product((n + 1 - i) for i in range(1, k + 1)) // factorial(k)
