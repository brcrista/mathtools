from functools import reduce
from core import lcm

def solution(n: int) -> int:
    """The smallest positive number divisible by all integers in [1, `n`]."""
    return reduce(lcm, range(1, n + 1))

def main():
    print(solution(20))

if __name__ == '__main__':
    main()
