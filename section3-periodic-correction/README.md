## `certify_H_nonconstancy.py`

Rigorous certificate for **Proposition 6**: `H(0) != H(log(3/2))`. Uses `python-flint`'s Arb/Acb
ball arithmetic throughout, not floating point, so the printed bounds are genuine, verified
enclosures, not numerical estimates.

**Run:** `python3 certify_H_nonconstancy.py`

**Expect:** a certified enclosure `-0.000377190280943987 < H(0)-H(log(3/2)) < -0.000377190280943985`,
proving the two values are distinct, with an explicit tail-majorant derivation printed along the
way. The script asserts these bounds itself; it exits with an `AssertionError` if they fail.
