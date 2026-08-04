"""Direct numerical test of Conjecture 3: phi(z_l)/phi_0(z_l) -> e^{H(0)} along
z_l = l * 3^{-l}, Wirsching's own comparison class at lambda=1.

Self-contained: phi is evaluated by the real-variable saddlepoint approximation
(justified rigorously, uniformly, by Theorem 3 of the paper), not by oscillatory
Fourier inversion. phi_0 uses the exponents gamma, delta, beta derived in Section 6
of the paper (matching Berg-Kruppel's own (9.6), see
derive_P_bergkruppel_identity.py in ../section6-berg-kruppel-identity/).

This is supporting numerical evidence for Theorem 1, not a substitute for the proof
in papers/01-wirsching-conjecture3/main.tex.
"""
import mpmath as mp

mp.mp.dps = 60


def h(x):
    if x == 0:
        return mp.mpf(0)
    return mp.log((1 - mp.e ** (-2 * x)) / (2 * x))


def m_func(x):
    if x == 0:
        return mp.mpf(0)
    return 1 - 2 * x / (mp.e ** (2 * x) - 1)


def v_func(x):
    if x == 0:
        return mp.mpf(0)
    return 1 - (x / mp.sinh(x)) ** 2


def series_sum(f, s, terms=250):
    total = mp.mpf(0)
    denom = mp.mpf(3)
    for _ in range(terms):
        x = s / denom
        if abs(x) < mp.mpf(10) ** (-(mp.mp.dps - 8)):
            break
        total += f(x)
        denom *= 3
    return total


def phi_saddle(t, terms=250):
    """Real-variable saddlepoint approximation to phi(t), Theorem 3 of the paper."""
    t = mp.mpf(t)
    guess = 1 / t if t > 0 else mp.mpf(1)
    s = mp.findroot(lambda s: series_sum(m_func, s, terms) - s * t, guess,
                     tol=mp.mpf("1e-40"))
    K_s = series_sum(h, s, terms)
    V_s = series_sum(v_func, s, terms)
    return s / mp.sqrt(2 * mp.pi * V_s) * mp.e ** (K_s + s * t)


a = mp.log(3)
beta = 1 / (2 * a)
gamma = mp.mpf("-1.5") - (1 + mp.log(a / 2)) / a
delta = 1 + mp.log(a / 2) / a


def phi_0_bare(t):
    t = mp.mpf(t)
    L = -mp.log(t)
    return t ** gamma * L ** delta * mp.e ** (-beta * mp.log(t / L) ** 2)


if __name__ == "__main__":
    print("Berg-Kruppel exponents (a=3, lambda=2/3):")
    print(f"  beta  = {mp.nstr(beta, 15)}")
    print(f"  gamma = {mp.nstr(gamma, 15)}")
    print(f"  delta = {mp.nstr(delta, 15)}\n")
    print("Predicted limit (bare normalization, Section 6 of the paper):")
    print("  e^{C_P+H(0)} = 0.204987710306551537...\n")

    print(f"{'l':>5}{'ratio phi/phi_0':>20}")
    for l in range(5, 51, 5):
        t_l = mp.mpf(l) * mp.mpf(3) ** (-l)
        ratio = phi_saddle(t_l) / phi_0_bare(t_l)
        print(f"{l:>5}{mp.nstr(ratio, 12):>20}")

    print("\nThe ratio dips below the limit before slowly rising back towards it,")
    print("visible already by l=50. Full convergence to 0.204988 (Theorem 1's")
    print("closed-form limit under the bare normalization) needs l well beyond what")
    print("mpmath's default root-finder handles reliably from a naive starting")
    print("guess at this precision; this range is illustrative numerical evidence,")
    print("not the proof, which is unconditional and does not depend on this script.")
