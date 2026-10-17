"""Triangle classification (sample solution).

Implements the Part 1 spec only:
  - is_valid_triangle(a, b, c) -> bool
  - classify_triangle(a, b, c) -> str
"""

import math


def is_valid_triangle(a, b, c) -> bool:
    """Return True only for a genuine (non-degenerate) triangle.

    All three sides must be positive numbers satisfying the strict triangle
    inequality. The degenerate case (the sum of two sides equals the third)
    is NOT valid. Non-numeric input is invalid rather than an exception.
    """
    try:
        if a <= 0 or b <= 0 or c <= 0:
            return False
        return (a + b > c) and (a + c > b) and (b + c > a)
    except TypeError:
        # Non-numeric side lengths can't form a triangle.
        return False


def classify_triangle(a, b, c) -> str:
    """Classify a triangle from its three side lengths.

    Returns "Invalid" for anything that isn't a valid triangle; otherwise
    "Equilateral", "Isosceles", or "Scalene", prefixed with "Right " when the
    sides satisfy the Pythagorean theorem (checked with math.isclose
    tolerance, never ==).
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"
    if a == b == c:
        return "Equilateral"
    x, y, z = sorted([a, b, c])
    right = math.isclose(x * x + y * y, z * z)
    base = "Isosceles" if (a == b or b == c or a == c) else "Scalene"
    return ("Right " if right else "") + base
