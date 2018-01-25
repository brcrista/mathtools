from typing import Iterator

def alphabetic_value(c: str) -> int:
    """The position of `c` in the Latin alphabet (case insensitive)."""
    return ord(c.upper()) - ord('A') + 1

def name_score(name: str, position: int) -> int:
    """
    The sum of alphabetic values of the letters in the name times the lexicographic position
    of the name in some sequence of names.
    """
    return sum(alphabetic_value(c) for c in name) * position

def tokenize_names(raw_names: str) -> Iterator[str]:
    for line in raw_names.splitlines():
        for name in line.split(','):
            token = name.strip('"')
            if token != '':
                yield token

def total_names_score(raw_names: str) -> int:
    sorted_names = sorted(tokenize_names(raw_names))
    return sum(name_score(name, i + 1) for i, name in enumerate(sorted_names))

def main():
    with open('names.txt') as names_file:
        print(total_names_score(names_file.read()))

if __name__ == '__main__':
    main()
