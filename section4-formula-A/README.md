## `verify_formula_A_bound.py`

Audit of the explicit constant chain behind **Theorem 3** (Formula (A)): the sector bounds of
Lemma 1 (checked against direct numerical differentiation of the log-density kernel, at real and
complex arguments), the two summed constants `A` (Lemma 2) and `F` (Lemma 4), and the assembled
error bound `E(N)` (monotonicity, `E(17) < 1`, and the asymptotic limit `sqrt(N)*E(N) -> 0.742358`).

This script checks the proof's own arithmetic; it does not re-derive the inequalities, which are
in the written proof (`papers/01-wirsching-conjecture3/main.tex`, Section 4, mirroring
`notes/H-006-formula-A-proof-2.md` in the main project repository).

**Run:** `python3 verify_formula_A_bound.py`

**Expect:** every assertion passes; a table of `E(N)` for `N` from `17` to `10^6`, strictly
decreasing, with `sqrt(N)*E(N)` converging to `0.742358`.
