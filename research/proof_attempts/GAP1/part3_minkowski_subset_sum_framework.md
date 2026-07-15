# Conjecture 3.1 — Recursive Function Attack

## The Core Recursive Equation for R₀

**Define:** R₀(M) = { subset sums of all divisors of M, including empty set = 0 }

**Theorem R (Recursive Structure):**
For prime p ∤ M:
```
R₀(M · p) = { r₀ + p · r₁ : r₀ ∈ R₀(M), r₁ ∈ R₀(M) }
```

For prime power p^a:
```
R₀(M · p^a) = { Σ_{j=0}^{a} p^j · r_j : each r_j ∈ R₀(M) }
```

**Proof:**
Divisors of M·p^a = { d · p^j : d | M, 0 ≤ j ≤ a } (since gcd(M,p)=1).
A subset S of these is determined by independent choices S_j ⊆ {d : d | M} for each j.
Sum = Σ_j p^j · (Σ S_j). And Σ S_j ∈ R₀(M) for each j independently. ∎

This is the **master recursive equation** for the achievable subset sums.

---

## Reformulating Conjecture 3.1

**Target:** Show E(Mq) ∈ R₀(M) for near-abundant deficient M, prime q ∤ M.

Let M = p₁^{a₁} · p₂^{a₂} · ... · p_r^{a_r}.

Apply Theorem R iteratively. Starting from the base:

```
R₀(1) = {0, 1}   (divisors of 1: just {1}, plus empty set = 0)
```

Then:
```
R₀(p₁^{a₁})       = { Σ_{j=0}^{a₁} p₁^j · ε_j : ε_j ∈ {0,1} }  (base-p₁ binary digits)

R₀(p₁^{a₁}·p₂^{a₂}) = { Σ_{j=0}^{a₂} p₂^j · r_j : r_j ∈ R₀(p₁^{a₁}) }

R₀(M)             = { Σ_{j=0}^{a_r} p_r^j · r_j : r_j ∈ R₀(M/p_r^{a_r}) }
```

So **E(Mq) ∈ R₀(M)** iff E(Mq) has a representation:
```
E(Mq) = Σ_{j=0}^{a_r} p_r^j · r_j,   r_j ∈ R₀(M')
```
where M' = M / p_r^{a_r}.

---

## The Digit Decomposition Function

**Define:** For integers T, base p, digit set D, define:

```
Rep(T, p, D) = true  iff  T = Σ_{j≥0} p^j · d_j  for some d_j ∈ D
```

**Recursive evaluation:**
```
Rep(T, p, D):
    d₀ = T mod p  (reduce mod p)
    if d₀ ∉ D: return false          ← digit check fails
    return Rep((T - d₀)/p, p, D)     ← recurse on quotient
```

Wait — this standard approach fails because our digit set D = R₀(M') can have elements > p.

**Corrected algorithm (greedy with carry):**

The digit r_j at position j is not constrained to [0, p-1] but to R₀(M') ⊆ [0, σ(M')].
So "digits" can overflow p. The representation is NOT base-p in the classical sense.

**Correct check:**
```
Rep_D(T, p, a, D):     # can T be written as Σ_{j=0}^{a} p^j d_j, d_j ∈ D?
    if a = 0: return (T ∈ D)
    for each d₀ ∈ D with d₀ ≤ T:
        if Rep_D(T - d₀, p, a-1, D) via shifted problem: ...
```

This is essentially the subset sum problem again on D. However, the STRUCTURE of D = R₀(M')
allows a much more efficient approach.

---

## The Key Structural Lemma

**Lemma Φ (Complement Closure):**
R₀(M) is closed under σ(M)-complement:
```
r ∈ R₀(M)  ⟹  σ(M) − r ∈ R₀(M)
```

**Proof:** If S ⊆ D(M) with Σ S = r, then the complement D(M) \ S has sum σ(M) − r. ∎

**Lemma Ψ (Translation by σ(M')):**
In the recursive representation R₀(M) = { Σ p^j r_j : r_j ∈ R₀(M') }:

If we replace r_j → σ(M') − r_j (complement each digit), the sum becomes:
```
Σ p^j (σ(M') − r_j) = σ(M') · Σ p^j − Σ p^j r_j = σ(M')·σ(p^a) − T = σ(M) − T
```

So: **T ∈ R₀(M) ⟺ σ(M) − T ∈ R₀(M)**.

This confirms Complement Closure for the full M. ✓

---

## Defining the Attack Function

**Define:** Φ(M, q) = "is E(Mq) representable as Σ p_r^j r_j with r_j ∈ R₀(M')?"

where p_r is the largest prime of M and M' = M/p_r^{a_r}.

**Recursive reduction:**

E(Mq) = σ(M) + q·E(M)   [excess recursion]

In terms of M = M'·p^a (p = p_r):

σ(M) = σ(M')·σ(p^a) = A · B   (where A = σ(M'), B = σ(p^a) = 1+p+...+p^a)

E(M) = AB − 2M'p^a

E(Mq) = AB + q(AB − 2M'p^a) = AB(1+q) − 2qM'p^a

**Extract base-p digit at position a (highest):**

Write E(Mq) = r_a · p^a + remainder.

r_a = floor(E(Mq) / p^a).

E(Mq) / p^a = AB(1+q)/p^a − 2qM'
= A·B/p^a·(1+q) − 2qM'
= A·(1+p+...+p^a)/p^a·(1+q) − 2qM'
= A·(p^{-a}+...+1)·(1+q) − 2qM'
→ A(1+q) − 2qM'   as a → ∞  [for finite a, there are lower-order terms]

For a = 1 (simplest case, M = M'·p):

E(M'pq) = A(p+1)(1+q) − 2qM'p

Digit at position 1: r₁ = floor(E(M'pq)/p).

Let's compute: E(M'pq) = A(p+1)(1+q) − 2qM'p.

r₁ = floor[A(p+1)(1+q)/p − 2qM'] = A(1+q) + floor[A(1+q)/p] − 2qM'

This is getting messy. Better approach: **define the problem as a recursion on r itself.**

---

## The Recursive Attack (Clean Form)

**Define:** For M = M'·p (one prime factor added at a time), p ∤ M':

```
Need: E(Mpq') ∈ R₀(Mp) = {r₀ + p·r₁ : r₀, r₁ ∈ R₀(M')}
```

So we need: E(Mpq') = r₀ + p·r₁ for some r₀, r₁ ∈ R₀(M').

E(Mpq') = σ(Mp) + q'·E(Mp)
= A(p+1) + q'(A(p+1) − 2M'p)
= A(p+1)(1+q') − 2q'M'p

So: r₀ + p·r₁ = A(p+1)(1+q') − 2q'M'p

Decompose: r₀ = E(Mpq') mod p (the "mod p" part)
           r₁ = (E(Mpq') − r₀)/p

**The mod p structure:**

E(Mpq') ≡ A(p+1)(1+q') − 2q'M'p  (mod p)
         ≡ A·1·(1+q') − 0         (mod p)    [since (p+1) ≡ 1, p ≡ 0 mod p]
         ≡ A(1+q')                 (mod p)

So r₀ ≡ A(1+q') (mod p).

For r₀ ∈ R₀(M'): we need A(1+q') mod p to be achievable as a residue mod p of some element of R₀(M').

**Key question:** Is A(1+q') mod p always in { r mod p : r ∈ R₀(M') }?

---

## The Residue Coverage Lemma

**Lemma Γ:** For M' odd with smallest prime factor p₁, every residue mod p₁ is achievable by R₀(M').

**Proof attempt:**
Divisors of M' include: 1 (contributes residue 1), p₁ (contributes 0), 1+p₁ ≡ 1+p₁ mod p₁... 

Actually R₀(M') mod p₁:
- {0}: empty subset (0 mod p₁ = 0)
- {1}: 1 mod p₁ = 1
- {p₁}: p₁ mod p₁ = 0 (same as empty? No, different elements)
- {1, p₁}: 1+p₁ ≡ 1 mod p₁

So residues 0 and 1 are achievable. But residue 2: need subset summing to something ≡ 2 mod p₁.

For p₁ = 3: need sum ≡ 2 mod 3. 
Divisors of M' include p₂ (next prime > 3). If p₂ ≡ 2 mod 3 (e.g., p₂ = 5: 5 ≡ 2 mod 3). ✓

So for M' containing prime 5: residue 2 mod 3 is achievable. ✓

For M' = 3^a: divisors are {1, 3, 9, ..., 3^a}. All ≡ 0 or 1 mod 3. Cannot achieve 2 mod 3!

**So Lemma Γ fails for prime powers.** But prime powers cannot be near-abundant (I(3^a) < 2 < 2q/(q+1) for any q), so they're excluded from our case!

---

## Key Structural Result

**Theorem Γ* (Residue Completeness for Near-Abundant M'):**

If M' is odd and I(M') > 2q/(q+1) for some prime q ≥ 11, then M' has at least 2 distinct prime factors.

For M' with at least 2 distinct odd prime factors p₁ < p₂:

Every residue mod p₁ is achieved in R₀(M'):
- Residue 0: use empty subset (or {p₁})
- Residue 1: use {1}  
- Residue 2: use {p₂} if p₂ ≡ 2 mod p₁, or combinations
- ...

For p₁ = 3, p₂ = 5: 5 ≡ 2 mod 3. So residues 0, 1, 2 all achievable. ✓  
For p₁ = 3, p₂ = 7: 7 ≡ 1 mod 3. Residue 2 needs {5} — but 5 ∤ M' if M' = 3^a·7^b. ✗

**Failure case:** M' = 3^a · 7^b. Both 3 ≡ 0 and 7 ≡ 1 mod 3. Cannot achieve 2 mod 3.

I(3^a · 7^b) ≤ (3/2)(7/6) = 7/4 = 1.75 < 11/6 ≈ 1.833 for q = 11.

So M' = 3^a · 7^b does NOT satisfy the near-abundant constraint for q = 11. Excluded! ✓

---

## The Sieve: Near-Abundant M' Forces Residue Completeness

**Conjecture Γ** (to prove): If M' is odd, I(M') > 2q/(q+1), q ≥ 11 prime, q ∤ M', then R₀(M') covers all residues mod p₁ (where p₁ = smallest prime factor of M').

**Evidence:**

| M' structure | I(M') bound | Achieves all mod-3 residues? |
|---|---|---|
| 3^a only | 3/2 = 1.5 < 1.83 | No (but excluded by near-abund.) |
| 3^a · 5^b | up to 15/8 = 1.875 > 1.83 | Yes: 5 ≡ 2 mod 3 ✓ |
| 3^a · 7^b | up to 7/4 = 1.75 < 1.83 | No (excluded) |
| 3^a · 5^b · 7^c | up to 35/16 = 2.19 > 1.83 | Yes: 5 ≡ 2 mod 3 ✓ |
| 3^a · 11^b | up to 11/6 ≈ 1.83 ≈ bound | Borderline |

**Pattern:** The near-abundant constraint forces M' to include a prime ≡ 2 mod 3, which gives residue completeness mod 3. This appears to generalize.

---

## Summary of Recursive Framework

```
Φ(M, q) = true  iff  E(Mq) ∈ R₀(M)

Recursive decomposition (M = M' · p):
   Φ(M'p, q) = true
   iff  E(M'pq) = r₀ + p·r₁  for some r₀, r₁ ∈ R₀(M')
   iff  [E(M'pq) mod p ∈ ResidueSet(R₀(M'), p)]
        AND Φ-like condition on (E(M'pq) - r₀)/p with digit set R₀(M')

Near-abundant constraint forces:
   M' has ≥ 2 distinct primes
   ⟹ R₀(M') covers all residues mod p₁
   ⟹ mod-p step always succeeds
   ⟹ recurse on smaller problem
```

**Open:** Prove the recursion terminates with "true" — i.e., at the base step R₀(M') always contains the final reduced target. This requires bounding the reduced target ≤ σ(M') at each step.

**Next file:** Prove the bound on the reduced target (that it stays in [0, σ(M')]) throughout the recursion, using the near-abundant constraint at each level.
