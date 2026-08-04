## `verify_envelope_lemma.py`

Independent, standalone audit of **Proposition 8** (the envelope estimate) and its inputs. Builds
`H` from the exact telescoping identity (Theorem 4) directly from the defining Laplace product,
without importing any other evaluator in this repository; certifies the coarse `H'`, `H''` bounds
used in the envelope proof via `python-flint` ball arithmetic; and compares the true and smooth
saddle locations at `tau = 20, 40, 80, 160`.

**Run:** `python3 verify_envelope_lemma.py`

**Expect:** `H(0)`, `H(log(3/2))`, `H(0.7)` printed to 35 digits, matching Section 3's values;
certified bounds `|H'| < 0.007`, `|H''| < 0.04`; and a table showing `B0*(w*-w0)` and
`B0*(g*-g0full)` both `O(1)` (i.e. the raw quantities are `O(1/B0)`), confirming the envelope
estimate's rate.
