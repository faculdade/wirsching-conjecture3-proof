## `derive_P_bergkruppel_identity.py`

Verifies **Proposition 9** and the closed-form constant `C_P` behind **Corollary 2**: evaluates the
exact smooth-saddle expression `P(tau)` and compares it against `log(phi_0,bare(e^{-tau}))` at
increasing `tau`, confirming the difference converges to the stated closed form `C_P`, and that
`P(tau) - log(phi_0,BK(e^{-tau}))` (the literal Berg-Kruppel-normalized comparison) converges to
`0` at the same rate.

**Run:** `python3 derive_P_bergkruppel_identity.py`

**Expect:** printed Berg-Kruppel parameters (`beta`, `gamma`, `delta`, `epsilon`, `const_bare`)
matching the paper's Section 6, and a table showing the two differences shrinking toward `0` (for
`P - log(phi_0,BK)`) and toward `const_bare = -0.9576743183...` (for `P - log(phi_0,bare)`) as `tau`
grows from `10` to `10^8`.
