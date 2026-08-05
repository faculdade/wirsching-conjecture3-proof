## `certify_H_nonconstancy.py`

Rigorous certificates for **Proposition 8** (`H(0) != H(log(3/2))`), and for the derivative bounds
of equation (3) and the oscillation `osc(H)` of that same proposition. Uses `python-flint`'s
Arb/Acb ball arithmetic throughout, not floating point, so the printed bounds are genuine, verified
enclosures, not numerical estimates.

**Run:** `python3 certify_H_nonconstancy.py`

**Expect:** a certified enclosure `-0.000377190280943987 < H(0)-H(log(3/2)) < -0.000377190280943985`;
then certified bounds `sup|H'| <= 0.0011977472315550332` and `sup|H''| <= 0.0068518962896650951`
(equation (3) of the paper), matched to the quoted values; then, on a grid of `N=2^20` points
combined with the certified Lipschitz bound, the same tight enclosure Proposition 8 states,
`osc(H) in [4.1874494771e-4, 4.1874620262e-4]` (matching down to the exact grid indices of the max
and min, 486746 and 1011118). Takes under a minute. The script asserts each bound itself; it exits
with an `AssertionError` if any fails.
