from itertools import count
from core import is_prime

def nth_prime(n: int) -> int:
    number_of_primes = 0
    for k in count(start=1):
        if is_prime(k):
            number_of_primes += 1
        if number_of_primes == n:
            return k

if __name__ == '__main__':
    print(nth_prime(10001))
