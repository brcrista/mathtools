import itertools
from typing import Iterable, List, TypeVar

_T = TypeVar('_T')

def take(n: int, iterable: Iterable[_T]) -> List[_T]:
    "Return the first `n` items of the iterable as a list"
    return list(itertools.islice(iterable, n))
