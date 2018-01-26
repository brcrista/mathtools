from core import eratosthenes

def sum_of_primes_below(n: int) -> int:
    """The sum of all primes below `n`."""
    return sum(eratosthenes(n))

if __name__ == '__main__':
    print(sum_of_primes_below(2000000))
