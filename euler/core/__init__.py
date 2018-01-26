"""
Project Euler likes to use certain patterns for representing its problems, like presenting a large blob of text that needs to be parsed into an array.
This module is for utility functions and classes that are useful for handling these Project Euler-specific situations.
"""

def parse_grid(grid: str) -> List[List[int]]:
    """
    Read a string representing a (possibly jagged) 2-D array of integers into a `List[List[int]]`.

    Rows in the grid should be separated by newlines and elements should be separated by spaces.
    """
    return [[int(element) for element in line.split()] for line in grid.splitlines() if line]

def in_bounds_2d(array_2d: List[List[int]], row_index: int, column_index: int) -> bool:
    """Whether `row_index`, `column_index` are in bounds for the possibly jagged `array_2d`."""
    return 0 <= row_index < len(array_2d) and 0 <= column_index < len(array_2d[row_index])
