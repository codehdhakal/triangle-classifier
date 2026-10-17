"""Acceptance test for the school-riddle customer scenario.

Customer: entrants type three side lengths and are told the shape and whether
it is buildable; invalid input shows a message instead of crashing; right
triangles are flagged (reinforced corners).
"""

from triangle import classify_triangle


def test_acceptance_customer_riddle():
    # Buildable shape, correctly named and flagged as right (reinforced corners).
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    # Not buildable -> "Invalid" message, no exception raised.
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(-1, 4, 4) == "Invalid"
