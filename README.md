# Triangle Classifier (sample solution)

Sample solution for the "triangle classifier" assignment: classify a triangle
from three side lengths, with unit tests, one acceptance test, and a Copilot
review log.

## How to run the tests

```bash
pip install -r requirements.txt
pytest
```

## Implementation notes

- `is_valid_triangle(a, b, c)` returns `True` only when all three sides are
  positive numbers satisfying the strict triangle inequality. The degenerate
  case (the sum of two sides equals the third) is **not** valid, and
  non-numeric input is treated as invalid rather than raising.
- `classify_triangle(a, b, c)` returns `"Invalid"` for anything that fails
  validation; otherwise `"Equilateral"`, `"Isosceles"`, or `"Scalene"`,
  prefixed with `"Right "` when the sides satisfy the Pythagorean theorem.
- The right-angle check uses `math.isclose` (default tolerance), never `==`,
  so float hypotenuses like `5 * math.sqrt(2)` classify correctly.

### Right-angle classes chosen

Only `"Right Scalene"` (e.g. 3-4-5) and `"Right Isosceles"` (e.g. 5-5-5√2)
can occur. An equilateral triangle can never be right: all three of its
angles are 60°, so none is 90°. Equivalently, `a² + a² = 2a²` can never equal
`a²` for `a > 0`, so the Pythagorean condition always fails for equal sides.

### Boundaries identified

- Side ≤ 0 (zero and negative) → invalid.
- Degenerate: the sum of two sides exactly equals the third, e.g. (2, 3, 5)
  → invalid.
- Float tolerance: exact `==` on `x² + y²` vs `z²` fails for irrational
  hypotenuses, so the right-angle boundary is decided by `math.isclose`.

## Copilot Review Log

Written while drafting `test_triangle.py` with GitHub Copilot autocomplete in
VS Code; every suggestion was checked against the spec table before keeping it.

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| test_invalid_zero_side | Yes | Kept | Suggestion matched the spec row exactly (`(0, 4, 5)` → `"Invalid"`). |
| test_invalid_negative_side | Yes | Kept | Correct assertion as suggested. |
| test_invalid_degenerate_boundary | Yes | Edited | Copilot suggested `(1, 2, 3)` expecting `"Invalid"` — correct per spec, but I changed it to `(2, 3, 5)` so the values make the degenerate boundary (two sides summing exactly to the third) obvious to a reader. |
| test_equilateral | Yes | Kept | `(5, 5, 5)` → `"Equilateral"`, no changes needed. |
| test_isosceles | Partial | Edited | Copilot completed the assertion as `"Isosceles"` but with sides `(5, 5, 5)` — that's equilateral, not isosceles. Fixed the sides to `(5, 5, 8)`; this is exactly the kind of mistake the spec table exists to catch. |
| test_scalene | Yes | Kept | `(4, 5, 6)` → `"Scalene"` as suggested. |
| test_right_scalene | Yes | Edited | Copilot suggested the test name `test_pythagorean`; renamed to `test_right_scalene` to use the spec's vocabulary. Assertion kept. |
| test_right_isosceles_non_integer_sides | Yes | Edited | Copilot's draft computed the hypotenuse then compared floats with `==` in a helper; deleted the helper — the test only asserts on the returned label, and the tolerance lives in the implementation per the spec. |
| test_non_numeric_input_is_invalid | No | — | Wrote manually; Copilot offered nothing useful for this edge since the spec table doesn't cover it. |

The catches that mattered: the isosceles sides Copilot proposed were actually
equilateral, and the `==`-on-floats helper would have baked the exact mistake
the spec warns against into the test suite.

## Acceptance criteria

Rewritten from the customer's paragraph ("school-grade riddle ... tell them
the shape and whether it's buildable ... don't crash ... flag right-angle
places ... correct every time"):

1. **Correct shape, every time** — for any three numeric side lengths,
   `classify_triangle` returns exactly the spec-table label, including the
   `"Right "` prefix for Pythagorean triples within tolerance
   (e.g. `classify_triangle(3, 4, 5) == "Right Scalene"`).
2. **Invalid input never crashes** — for any side ≤ 0, a violated or
   degenerate triangle inequality, or non-numeric input,
   `classify_triangle` returns `"Invalid"` instead of raising an exception.
3. **Right angles are flagged** — any valid right triangle's label starts
   with `"Right "`, so the riddle app can mark those entries as needing
   reinforced corners.

`test_acceptance.py` covers criteria 1–2 end to end through `classify_triangle`.

## AI-use statement

I used GitHub Copilot (autocomplete in VS Code) while drafting the unit tests
in `test_triangle.py`, and I reviewed every suggestion against the spec table
before keeping it: I accepted suggestions that matched the spec, edited three
(wrong side lengths on the isosceles test, a test rename to spec vocabulary,
and removing a float `==` helper), and wrote the non-numeric edge test
manually. I wrote `triangle.py`, the acceptance criteria,
`test_acceptance.py`, and this README myself without AI assistance. All kept
suggestions were verified by running the full test suite.
