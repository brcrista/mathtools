from functools import reduce
from itertools import chain
from math import factorial, floor, gcd, sqrt
from operator import mul
from typing import overload, Any, Callable, List, Iterator, Optional, Tuple, TypeVar

T = TypeVar('T')

def assert_natural(n: int) -> None:
    """Raise a `ValueError` if `n` is not a natural number (starting with 1)."""
    if not (isinstance(n, int) and n >= 1):
        raise ValueError(f'`n` was {n} (must be a natural number)')

def divides(a: int, b: int) -> bool:
    """Return `True` iff `a` is a multiple of `b`."""
    return a % b == 0

def even(n: int) -> bool:
    """Whether an integer `n` is even."""
    return divides(n, 2)

def odd(n: int) -> bool:
    """Whether an integer `n` is odd."""
    return even(n + 1)

def factor_pairs(n: int) -> List[Tuple[int, int]]:
    """The pairs of factors of a natural number `n`."""
    assert_natural(n)
    return [(x, n // x) for x in range(1, floor(sqrt(n)) + 1) if divides(n, x)]

def factors(n: int) -> List[int]:
    """The factors of `n`."""
    return sorted(set(chain.from_iterable(factor_pairs(n))))

def proper_divisors(n: int) -> List[int]:
    return factors(n)[:-1]

def is_prime(n: int) -> bool:
    """Whether a natural number `n` is prime."""
    return n > 1 and factors(n) == [1, n]

def prime_factorization(n: int) -> List[int]:
    """The prime factors of `n`, including duplicates."""
    if n == 1:
        return []
    else:
        first_prime = next(fac for fac in factors(n) if is_prime(fac))
        return [first_prime] + prime_factorization(n // first_prime)

def eratosthenes(n: int) -> List[int]:
    """All primes less than `n`, computed with the Sieve of Eratosthenes."""
    maybe_prime = [False] + [False] + [True for k in range(2, n)]
    for i in range(2, n):
        if maybe_prime[i]:
            for j in range(2 * i, n, i):
                maybe_prime[j] = False
    return [k for k in range(2, n) if maybe_prime[k]]

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

def lcm(a: int, b: int) -> int:
    """The least common multiple of `a` and `b`."""
    if a == 0 or b == 0:
        return 0
    else:
        return a * b // gcd(a, b)

def binomial_coefficient(n: int, k: int) -> int:
    """The binomial coefficient C(n, k)."""
    return product((n + 1 - i) for i in range(1, k + 1)) // factorial(k)

def is_iterable(x: Any) -> bool:
    return hasattr(x, '__iter__')

def first(x):
    return x[0]

def second(x):
    return x[1]

def identity(x: T) -> T:
    """The identity function."""
    return x

def compose(f, g):
    return lambda *args: f(g(*args))

def argmax(f, args, *, key=identity):
    """
    The element in `args` that produces the largest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f`  are maximal, returns the first set of arguments in `args`
    that produces the maximal value of `f`.
    """
    mapping = [(f(*x), x) if is_iterable(x) else (f(x), x) for x in args]
    return second(max(mapping, key=compose(key, first)))

def argmin(f, args, *, key=identity):
    """
    The element in `args` that produces the smallest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f`  are minimal, returns the first set of arguments in `args`
    that produces the minimal value of `f`.
    """
    mapping = [(f(*x), x) if is_iterable(x) else (f(x), x) for x in args]
    return second(min(mapping, key=compose(key, first)))

def parse_grid(grid: str) -> List[List[int]]:
    """
    Read a string representing a (possibly jagged) 2-D array of integers into a `List[List[int]]`.

    Rows in the grid should be separated by newlines and elements should be separated by spaces.
    """
    return [[int(element) for element in line.split()] for line in grid.splitlines() if line]

def in_bounds_2d(array_2d: List[List[int]], row_index: int, column_index: int) -> bool:
    """Whether `row_index`, `column_index` are in bounds for the possibly jagged `array_2d`."""
    return 0 <= row_index < len(array_2d) and 0 <= column_index < len(array_2d[row_index])
