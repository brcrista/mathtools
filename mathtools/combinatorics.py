from math import factorial
from typing import Callable, Iterator, Optional, TypeVar
from mathtools import product

T = TypeVar('T')

def recurrence(start: T, func: Callable[[T], Optional[T]]) -> Iterator[T]:
    """
    Return an `Iterator` beginning with `start` where each element is created
    by applying `func` to the previous element.

    Iteration stops when a `None` value is reached.
    """
    current = start
    while current is not None:
        yield current
        current = func(current)

def fibonacci_numbers() -> Iterator[int]:
    """The infinite sequence of Fibonacci numbers: 1, 2, 3, 5, 8, ..."""
    last1 = 1
    last2 = 0
    while True:
        fib = last1 + last2
        last2 = last1
        last1 = fib
        yield fib

def binomial_coefficient(n: int, k: int) -> int:
    """The binomial coefficient C(n, k)."""
    return product((n + 1 - i) for i in range(1, k + 1)) // factorial(k)
