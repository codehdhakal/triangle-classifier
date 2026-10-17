"""Acceptance test for the stained-glass studio customer scenario.

Customer: clients enter three side lengths and are told the shape and whether
the piece is buildable; invalid input shows a message instead of crashing;
right-angle pieces are flagged (reinforced corners); a wrong answer means a
ruined pane.
"""

from triangle import classify_triangle


def test_acceptance_stained_glass_studio():
    # Buildable piece, correctly named and flagged as right (reinforced corners).
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    # Not buildable -> "Invalid" message, no exception raised.
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(-1, 4, 4) == "Invalid"
