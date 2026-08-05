## `verify_formula_A_bound.py`

Audit of the explicit constant chain behind **Theorem 13** (uniform saddlepoint asymptotic): the
sector bounds of Lemma 9 (checked against direct numerical differentiation of the log-density
kernel, at real and complex arguments), the two summed constants `A_V` (Lemma 10) and `F` (Lemma
12, whose constant `2N+10.559` supersedes an earlier, incorrect `2N+3.7442`), and the assembled
error bound `E(N)` (monotonicity, `E(19) < 1` with `N_0=19` sharp since `E(18) > 1`, and the
asymptotic limit `sqrt(N)*E(N) -> 0.742358`).

This script checks the proof's own arithmetic; it does not re-derive the inequalities, which are
in the written proof (`papers/01-wirsching-conjecture3/main.tex`, Section 4, mirroring
`notes/H-006-formula-A-proof-2.md` in the main project repository).

**Run:** `python3 verify_formula_A_bound.py`

**Expect:** every assertion passes; a table of `E(N)` for `N` from `19` to `10^6`, strictly
decreasing, with `sqrt(N)*E(N)` converging to `0.742358`.
