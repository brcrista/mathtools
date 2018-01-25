from itertools import count
from itertools import product as cartesian_product
from functools import partial
from typing import Callable

from core import argmax, is_prime, product

def quadratic(n: int, a: int, b: int) -> int:
    return (n * n) + (a * n) + b

def consecutive_primes(unary_func: Callable[[int], int]) -> int:
    """
    The number of consecutive prime outputs produced by `unary_func`
    from inputs starting with 0.
    """
    for k in count():
        if not is_prime(unary_func(k)):
            return k

def quadratic_primes() -> int:
    f = lambda x, y: consecutive_primes(partial(quadratic, a=x, b=y))
    return product(argmax(f, cartesian_product(range(-999, 1000), range(-1000, 1001))))

def main():
    print(quadratic_primes())

if __name__ == '__main__':
    main()
