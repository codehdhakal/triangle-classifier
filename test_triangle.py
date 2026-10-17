"""Unit tests for triangle.py.

Covers every row of the Part 1 spec table, the degenerate boundary case,
and a right-triangle test with non-integer sides.
"""

import math

from triangle import classify_triangle, is_valid_triangle


def test_invalid_zero_side():
    assert not is_valid_triangle(0, 4, 5)
    assert classify_triangle(0, 4, 5) == "Invalid"


def test_invalid_negative_side():
    assert classify_triangle(-3, 4, 5) == "Invalid"


def test_invalid_degenerate_boundary():
    # Boundary: the sum of two sides EQUALS the third -> not a triangle.
    assert not is_valid_triangle(2, 3, 5)
    assert classify_triangle(2, 3, 5) == "Invalid"


def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"


def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"


def test_right_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"


def test_right_isosceles_non_integer_sides():
    hyp = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hyp) == "Right Isosceles"


def test_non_numeric_input_is_invalid():
    assert classify_triangle("3", 4, 5) == "Invalid"
    assert not is_valid_triangle(None, 4, 5)
