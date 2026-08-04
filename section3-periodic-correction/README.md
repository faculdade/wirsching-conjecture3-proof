## `certify_H_nonconstancy.py`

Rigorous certificates for **Theorem 8** (`H(0) != H(log(3/2))`), and for the derivative bounds of
equation (3) and the oscillation `osc(H)` of that same theorem. Uses `python-flint`'s Arb/Acb ball
arithmetic throughout, not floating point, so the printed bounds are genuine, verified enclosures,
not numerical estimates.

**Run:** `python3 certify_H_nonconstancy.py`

**Expect:** a certified enclosure `-0.000377190280943987 < H(0)-H(log(3/2)) < -0.000377190280943985`;
then certified bounds `sup|H'| <= 0.0011977472315550332` and `sup|H''| <= 0.0068518962896650951`
(equation (3) of the paper), matched to the quoted values; then a grid-based lower bound on
`osc(H)`, confirming it is bounded well away from 0 (a coarser check than the paper's own tight
enclosure, included for an independent cross-check). The script asserts each bound itself; it
exits with an `AssertionError` if any fails.
