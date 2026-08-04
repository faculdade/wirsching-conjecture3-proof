# Reproducibility repository: Wirsching's Conjecture 3

Companion code for the paper *"Wirsching's Conjecture 3, and the periodic correction to
Berg-Kruppel's density asymptotic"* (Renato Augusto Tavares). Every numerical claim in the paper is
backed by a script here that anyone can run and check against the values quoted in the text.

## Requirements

```
pip install mpmath python-flint
```

`python-flint` (Arb/Acb ball arithmetic) is used only where a genuinely certified, rigorous
enclosure is claimed (Sections 3, 5); everything else uses `mpmath` at high working precision.

## Layout

Organized by the paper's section numbers. Each folder has its own short README.

- `section1-conjecture3-numerical/` — direct numerical evidence for Theorem 1 (Conjecture 3),
  computing `phi(z_l)/phi_0(z_l)` along Wirsching's own sequence.
- `section3-periodic-correction/` — the rigorous ball-arithmetic certificate that `H` is not
  constant (Proposition 6).
- `section4-formula-A/` — audit of the explicit constant chain behind Theorem 3 (Formula (A)).
- `section5-envelope-lemma/` — independent audit of the envelope estimate (Proposition 8),
  including the certified bounds on `H'`, `H''`.
- `section6-berg-kruppel-identity/` — verification of the exact `P`-Berg-Kruppel identity and the
  closed-form constant `C_P` (Proposition 9, Corollary 2).

## Running everything

```
for d in section*/; do
  echo "=== $d ==="
  (cd "$d" && for f in *.py; do python3 "$f"; done)
done
```

Every script is self-contained (no imports from this repository's other files, no hardcoded
paths) and prints its own pass/fail assertions where the claim is a rigorous inequality.

## The paper

`main.tex` and `main.pdf` are in the main project repository, `papers/01-wirsching-conjecture3/`.
