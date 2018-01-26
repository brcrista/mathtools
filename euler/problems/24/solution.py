from itertools import permutations
from typing import Iterator

def digits_to_int(digits: Iterator[int]) -> int:
    return int(''.join(map(str, digits)))

def nth_lexicographic_permutation(elements: Iterator[int], n: int) -> int:
    """
    Select the `n`th permutation from the lexicographic ordering of the permutations of `elements`.
    """
    for i, p in enumerate(permutations(elements)):
        if i == n - 1:
            return digits_to_int(p)
    return None

def main():
    print(nth_lexicographic_permutation(range(0, 10), 1000000))

if __name__ == '__main__':
    main()
