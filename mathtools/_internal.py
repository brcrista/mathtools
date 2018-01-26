from typing import Any

def is_iterable(x: Any) -> bool:
    return hasattr(x, '__iter__')
