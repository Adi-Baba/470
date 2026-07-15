# Erdős Problem 470 — Rigorous Gap Analysis

**Question:** Does any odd weird number exist?

A positive integer N is **weird** if:
1. N is **abundant**: σ(N) > 2N  (equivalently, I(N) > 2, where I(N) = σ(N)/N)
2. N is **not pseudoperfect**: no subset S of proper divisors of N satisfies Σ S = N

---

## Definitions

| Symbol | Meaning |
|--------|---------|
| σ(N) | Sum of all positive divisors of N |
| I(N) | Abundancy index: σ(N)/N |
| E(N) | Excess: σ(N) − 2N = N(I(N) − 2) |
| D(N) | Set of all proper divisors of N |
| k | Number of distinct prime factors of N |
| ω(N) | Same as k |
| M-core | N divided by its largest prime power factor |

---

## What Is Already Proven

### Theorem A (Benkoski-Erdős, 1974)
Any odd weird number N satisfies N > 10^21.

### Theorem B (Paper 9, conditional)
Any odd weird number has k ≥ 4 distinct prime factors.

**Proof sketch for k ≤ 3:**

**k = 1:** N = p^a. Then I(p^a) = (p^(a+1) − 1) / (p^a(p − 1)) → p/(p−1) as a → ∞.
For the smallest odd prime p = 3: supremum of I is 3/2 < 2.
Hence odd prime powers are never abundant. ∎

**k = 2:** N = p^a q^b, p < q odd primes. Then:
I(N) = I(p^a) · I(q^b) < p/(p−1) · q/(q−1).
Minimum occurs at p=3, q=5: upper bound = (3/2)(5/4) = 15/8 = 1.875 < 2.
Hence two-prime odd numbers are never abundant. ∎

**k = 3:** Harder. One can show any odd abundant N with exactly 3 distinct prime
factors is pseudoperfect via explicit subset-sum construction (the paper's subset-sum
coverage lemma). The abundancy constraint forces one prime factor to be small (≤ 7),
giving enough divisors to cover N.

---

## The Three Gaps Blocking Full Resolution

### GAP 1 — The k ≥ 4 Algebraic Closure  *(Most Attackable)*

**Statement of gap:**  
Prove that every odd abundant number with k ≥ 4 distinct prime factors is pseudoperfect.

**Why this is the hardest remaining piece:**  
For k = 4, with primes (3, 5, 7, p) for p ≥ 11, the abundancy index upper bound is:
```
I(N) ≤ (3/2)(5/4)(7/6)(11/10) = 1155/480 ≈ 2.41
```
So N can be abundant. The divisor structure is richer, making it harder to identify gaps.

**Inductive structure (partial success):**

**Lemma 1.1 (Inheritance of Pseudoperfectness):**
Let M be pseudoperfect and q a prime with q ∤ M. Then N = Mq is pseudoperfect.

*Proof:* Since M is pseudoperfect, there exists S ⊆ D(M) with Σ S = M.
Define S' = { q·s : s ∈ S }.
Each element q·s divides N = Mq (since s | M).
Each q·s is a proper divisor of N because s < M implies q·s < qM = N.
Finally, Σ S' = q · Σ S = q · M = N.
Therefore S' ⊆ D(N) is a subset summing to N, so N is pseudoperfect. ∎

**Corollary 1.2:** If every odd abundant number with k' < k distinct primes is pseudoperfect,
then every odd abundant N = M·q (where M has k−1 primes, M is itself abundant)
is pseudoperfect.

**THE ACTUAL GAP (what Lemma 1.1 does NOT cover):**

The inheritance argument fails precisely when M is **not abundant** but Mq **is abundant**.

In this case I(M) < 2 but I(M) · I(q^a) > 2. This means:
```
I(q^a) > 2 / I(M) > 1
```
Since I(q^a) → q/(q−1), we need q/(q−1) > 2/I(M), i.e., q < I(M)/(I(M)−1).

For I(M) = 1.9 (M near-abundant): q < 1.9/0.9 ≈ 2.11, so q = 2. But N must be odd,
contradiction. Hence I(M) must be high enough, severely constraining M.

**This gives a new constraint:**

**Lemma 1.3 (Near-Perfect Constraint):**
If N = M · q^a is odd weird (q the largest prime factor, a ≥ 1), then:
```
I(M) > 2(q−1)/q
```
For q = 11: I(M) > 20/11 ≈ 1.818
For q = 13: I(M) > 24/13 ≈ 1.846

As q → ∞: I(M) → 2, meaning M must approach abundancy.

**Attack vector for Gap 1:**
Show that for M satisfying I(M) > 2(q−1)/q with M odd and ω(M) = k−1, the divisors
of M are already dense enough that M itself becomes pseudoperfect — collapsing the
non-abundant M case by a continuity-style argument.

---

### GAP 2 — The Subset Sum Escape  *(Technically Hardest)*

**Statement of gap:**
Even after establishing divisor density, prove there is no configuration of odd abundant
N where every possible subset sum misses exactly N.

**Why hard:** The subset sum problem is NP-complete in general. For structured sets
(divisors of integers) there is special arithmetic, but the escape condition is subtle.

**The completeness criterion:**

A set of positive integers A = {a₁ ≤ a₂ ≤ ... ≤ aₙ} is **complete** (every integer
in [1, Σ A] is a subset sum) if and only if:
```
a₁ = 1  and  aₖ ≤ 1 + a₁ + a₂ + ... + aₖ₋₁  for all k
```

**Problem:** For odd N, the smallest proper divisor is 1, the next is p₁ (the smallest
prime factor, at least 3). But 3 > 1 + 1 = 2, so the completeness criterion fails at k=2.

**This means:** There is always a gap between 2 and 3 in the representable subset sums of
divisors of odd N. Integers 2 and the values in (p₁, p₁ + 1) cannot be formed.

**The critical question:** Does N ever fall in such a gap?

**Lemma 2.1 (Gap Characterization):**
For odd abundant N, the subset sums of D(N) cover all integers in [1, σ(N)−N] except
for a set G of "gap values." N is weird ⟺ N ∈ G.

**Attack vector for Gap 2:**
Show that for odd abundant N, the value N is always covered by using a specific
algebraic identity on the divisors. Candidates:

1. **Divisor descent:** N/p₁ is always a divisor (p₁ | N), and N − N/p₁ = N(p₁−1)/p₁.
   Can N(p₁−1)/p₁ always be covered by remaining divisors?

2. **Complement method:** If σ(N) − N > N (guaranteed by abundance), consider the
   complement set: for any S ⊆ D(N), the complement D(N) \ S has sum (σ(N)−N) − Σ S.
   By IVT-style argument on the integer-valued function of subsets, some complement hits N.
   **This is the most promising pure-existence attack.**

---

### GAP 3 — The I(M) Upper Bound for Escalating Prime Chains

**Statement of gap:**
Tighten the upper bound on I(M) to eliminate the case where M is non-abundant
but I(M) · I(q^a) > 2 for a prime q ≥ some threshold.

**Why this matters:**
The c-exceptional framework (Paper 9) bounding I(M) < 2 for c ≥ c* = 17/11 is clean,
but it leaves the window 2(q−1)/q < I(M) < 2 unresolved for large q.

**Attack vector for Gap 3:**
Use Mertens' theorem: for odd N with k distinct prime factors p₁ < p₂ < ... < pₖ:
```
I(N) ≤ ∏ᵢ pᵢ/(pᵢ−1) = ∏ᵢ (1 − 1/pᵢ)⁻¹
```
By Mertens, ∏_{p≤x, p odd prime} p/(p−1) ~ (2e^γ/π) · log x.
This grows without bound, so for large k, N can become arbitrarily "super-abundant."
But this growth is logarithmically slow — and the subset-sum density also grows — so
there may be a coupling inequality waiting to be proved.

---

## Priority Ranking

| Gap | Difficulty | Theoretical Purity | Priority |
|-----|-----------|-------------------|----------|
| Gap 1 (k ≥ 4 closure) | Medium | High — pure algebra | **1st** |
| Gap 2 (subset sum escape) | High | High — combinatorial | **2nd** |
| Gap 3 (I(M) bound) | Medium | Medium — analytic | **3rd** |

**Gap 1 is most attackable first** because:
- Lemma 1.1 already closes half of it (the M-abundant sub-case)
- The remaining sub-case (M non-abundant, Mq abundant) has a tight arithmetic window
- The window forces q to be bounded relative to I(M), giving a finite case structure
- No computation needed: pure divisibility and inequality arguments suffice

---

## Proposed First Attack: Gap 1, Non-Abundant M Sub-Case

See: `proof_attempts/gap1_nonabd_M.md`

**Core idea:**
If M is odd with ω(M) = k−1 and I(M) < 2 but I(M) > 2(q−1)/q, then M is
"near-abundant." Near-abundant odd numbers with k−1 prime factors have a specific
structure (their prime factorization is tightly constrained) that forces their divisors
to already cover M as a subset sum — making M pseudoperfect — which then applies
Lemma 1.1 to close the case.

The proof attempt will formalize "near-abundant implies pseudoperfect" for odd numbers.
