from itertools import accumulate, count
from typing import Iterator

from core import factors

def triangle_numbers() -> Iterator[int]:
    """The infinite sequence of triangle numbers."""
    return accumulate(count(1))

def first_triangle_number_with_more_divisors_than(n: int) -> int:
    """The first triangle number with more than `n` divisors."""
    return next(filter(lambda x: len(factors(x)) > n, triangle_numbers()))

def main():
    print(first_triangle_number_with_more_divisors_than(500))

if __name__ == '__main__':
    main()
