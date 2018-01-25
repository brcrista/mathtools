from itertools import takewhile
from core import even, fibonacci_numbers

def solution(n: int) -> int:
    """The sum of even Fibonacci numbers less than `n`."""
    return sum(fib for fib in takewhile(lambda x: x < n, fibonacci_numbers()) if even(fib))

def main():
    print(solution(4000000))

if __name__ == '__main__':
    main()
