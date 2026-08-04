## `conjecture3_numerical_sweep.py`

Numerical evidence for **Theorem 1** (Conjecture 3). Computes `phi(z_l)/phi_0(z_l)` for
`z_l = l * 3^{-l}`, `l = 5..50`, using a self-contained real-variable saddlepoint evaluator for
`phi` (justified rigorously by Theorem 13, "Formula (A)") and the Berg-Kruppel exponents derived
in Section 6.

**Run:** `python3 conjecture3_numerical_sweep.py`

**Expect:** the ratio dips to about `0.1827` near `l=20` and then rises slowly back toward the
theorem's closed-form limit, `0.204988` (bare normalization). Full numerical convergence needs `l`
well beyond what a naive root-finder handles reliably at this precision; the theorem itself does
not depend on this script; it is illustrative supporting evidence, not a proof.
