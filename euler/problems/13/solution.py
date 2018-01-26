from typing import Iterator

def read_numbers_from_file(filename: str) -> Iterator[int]:
    """Read the list of 50-digit numbers from `filename`"""
    with open(filename) as fd:
        for line in fd.readlines():
            yield int(line)

def first_10_digits(n: int) -> str:
    return str(n)[0:10]

def large_sum():
    return first_10_digits(sum(read_numbers_from_file('numbers.txt')))

def main():
    print(large_sum())

if __name__ == '__main__':
    main()
