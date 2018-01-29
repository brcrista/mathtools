from typing import Any, TypeVar

T = TypeVar('T')

def _is_iterable(x: Any) -> bool:
    return hasattr(x, '__iter__')

def first(x):
    return x[0]

def second(x):
    return x[1]

def identity(x: T) -> T:
    """The identity function."""
    return x

def compose(f, g):
    """
    Create the composition of `f` and `g`, where the output of `g` is passed to `f`.

    >>> def f(x):
    ...     return 2 * x
    >>> def g(x, y):
    ...     return x - y
    >>> compose(f, g)(1, 2)
    -2
    """
    return lambda *args: f(g(*args))

def argmax(f, args, *, key=identity):
    """
    The element in `args` that produces the largest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f` are maximal, returns the first set of arguments in `args`
    that produces the maximal value of `f`.

    >>> argmax(identity, [0, 1, 5, 3])
    5
    >>> argmax(lambda x, y: x + y, [(0, 1), (1, 5), (3, 2)])
    (1, 5)
    """
    mapping = [(f(*x), x) if _is_iterable(x) else (f(x), x) for x in args]
    return second(max(mapping, key=compose(key, first)))

def argmin(f, args, *, key=identity):
    """
    The element in `args` that produces the smallest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f` are minimal, returns the first set of arguments in `args`
    that produces the minimal value of `f`.

    >>> argmin(identity, [0, 1, 5, 3])
    0
    >>> argmin(lambda x, y: x + y, [(0, 1), (1, 5), (3, 2)])
    (0, 1)
    """
    mapping = [(f(*x), x) if _is_iterable(x) else (f(x), x) for x in args]
    return second(min(mapping, key=compose(key, first)))
