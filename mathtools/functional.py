from typing import TypeVar
from _internal import is_iterable

T = TypeVar('T')

def first(x):
    return x[0]

def second(x):
    return x[1]

def identity(x: T) -> T:
    """The identity function."""
    return x

def compose(f, g):
    return lambda *args: f(g(*args))

def argmax(f, args, *, key=identity):
    """
    The element in `args` that produces the largest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f` are maximal, returns the first set of arguments in `args`
    that produces the maximal value of `f`.
    """
    mapping = [(f(*x), x) if is_iterable(x) else (f(x), x) for x in args]
    return second(max(mapping, key=compose(key, first)))

def argmin(f, args, *, key=identity):
    """
    The element in `args` that produces the smallest output of `f`.
    Each element of `args` should be an iterable of the parameter types of `f`.
    If two values of `f` are minimal, returns the first set of arguments in `args`
    that produces the minimal value of `f`.
    """
    mapping = [(f(*x), x) if is_iterable(x) else (f(x), x) for x in args]
    return second(min(mapping, key=compose(key, first)))
