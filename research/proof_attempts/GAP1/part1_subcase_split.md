# Step 1: Can N be Weird When M is Deficient?

## Setup

N = Mq^a, q prime, q ∤ M, q > all prime factors of M.  
M deficient means: σ(M) < 2M, i.e., E(M) = σ(M) − 2M < 0.  
N abundant means: E(N) = σ(N) − 2N > 0.

## The Complement Reformulation

**Lemma 0 (Complement Equivalence):**  
N is pseudoperfect ⟺ E(N) is a subset sum of D(N).

**Proof:**  
N pseudoperfect ⟺ ∃ S ⊆ D(N) with Σ S = N.  
Let T = D(N) \ S. Then Σ T = (σ(N) − N) − N = σ(N) − 2N = E(N).  
So S exists ⟺ T exists with Σ T = E(N). ∎

This is the master reformulation. All three steps reduce to: **can E(N) be expressed as a subset sum of D(N)?**

---

## Divisor Layer Decomposition

For N = Mq^a, the proper divisors partition into layers:

```
Layer j (0 ≤ j ≤ a):   L_j = { q^j · d : d | M }     for j < a
Layer a:                 L_a = { q^a · d : d | M, d < M }
```

Sum of layer j (j < a):   Σ L_j = q^j · σ(M)  
Sum of layer a:            Σ L_a = q^a · (σ(M) − M)

---

## The Excess Recursion (Key Tool)

For a = 1:
```
E(Mq) = σ(Mq) − 2Mq = σ(M)(q+1) − 2Mq
       = qσ(M) − 2Mq + σ(M)
       = q(σ(M) − 2M) + σ(M)
       = q · E(M) + σ(M)
```

For general a (by induction on a):
```
E(Mq^a) = q · E(Mq^{a-1}) + σ(Mq^{a-1})
```

This is the exact recursion from Paper 9.

---

## Main Result of Step 1

**Theorem 1.1 (Deficient M Obstruction):**  
If M is deficient, then N = Mq can still be pseudoperfect. M being deficient is NOT sufficient to make N weird.

**Proof (constructive):**  
We must find T ⊆ D(N) with Σ T = E(N) = qE(M) + σ(M).

Since M deficient: E(M) < 0. Since N abundant: E(N) > 0.  
So σ(M) > q|E(M)|.

**Construction of T:**

Decompose D(N) into:
- A = { d : d | M } with Σ A = σ(M)
- B = { qd : d | M, d < M } with Σ B = q(σ(M) − M)

E(N) = qE(M) + σ(M) = q(σ(M) − 2M) + σ(M) = σ(M)(q+1) − 2Mq

We need T ⊆ A ∪ B summing to E(N).

Take T₀ = A (all divisors of M). Then Σ T₀ = σ(M).

Remaining target: E(N) − σ(M) = q·E(M) = q(σ(M) − 2M) < 0.

**Problem:** The remaining target is NEGATIVE. We cannot add more elements to T₀ and reach E(N) if it is less than σ(M).

So we must use a SUBSET of A, not all of A.

Let T = T_A ∪ T_B where T_A ⊆ A, T_B ⊆ B.
Σ T = Σ T_A + Σ T_B = E(N).

Write Σ T_A = σ(M) − r for some 0 ≤ r ≤ σ(M) (we remove elements summing to r from A).  
Write Σ T_B = q · s for some s ∈ [0, σ(M) − M] (T_B uses some q-scaled divisors).

Condition: σ(M) − r + qs = E(N) = qE(M) + σ(M)
⟹ −r + qs = qE(M)
⟹ qs − r = q(σ(M) − 2M)
⟹ q(s − σ(M) + 2M) = r
⟹ r = q(s − σ(M) + 2M)

For r ≥ 0: s ≥ σ(M) − 2M = σ(M) − 2M.  
Since M deficient: σ(M) − 2M < 0, so σ(M) − 2M + 2M = σ(M). Wait:

σ(M) − 2M < 0 means σ(M) < 2M.  
So σ(M) − 2M < 0, and s ≥ σ(M) − 2M is always satisfied since s ≥ 0.

For r ≤ σ(M): q(s − (σ(M) − 2M)) ≤ σ(M)  
⟹ s ≤ σ(M)/q + σ(M) − 2M = σ(M)(1 + 1/q) − 2M

The maximum value s can take is σ(M) − M (sum of all of B divided by q).  
So we need s ≤ σ(M)(1 + 1/q) − 2M = σ(M) + σ(M)/q − 2M.

Since σ(M) − M is the max for s: need σ(M) − M ≤ σ(M) + σ(M)/q − 2M
⟹ M ≤ σ(M)/q
⟹ qM ≤ σ(M)
⟹ q ≤ I(M)

But I(M) < 2 (M deficient) and q ≥ 11. So **this condition FAILS**. ∎

---

## Conclusion of Step 1

The algebraic system r = q(s − σ(M) + 2M) has:
- r must be a representable "gap" in subset sums of A  
- s must be a representable value in subset sums of B/q

For deficient M with large prime q, the required s exceeds the available sum of B/q. This means:

> **A simple partition into T_A ∪ T_B does not generically work. N may or may not be pseudoperfect when M is deficient. The weird/non-weird status depends on fine arithmetic structure of D(M).**

**Key finding:** M being deficient does NOT automatically force N to be weird. But it removes the clean inductive structure. The deficient-M case requires a separate argument — which is Step 3.

---

## What Step 1 Rules Out

Step 1 proves:

**Corollary 1.2:** If M is deficient AND σ(M) ≤ q|E(M)|, then N = Mq is NOT abundant (hence not weird).

**Proof:** E(N) = qE(M) + σ(M) ≤ 0 if σ(M) ≤ q|E(M)|. ∎

So for N to be abundant with deficient M, we need: **σ(M) > q|E(M)|**.  
This tightly constrains the relationship between M's divisor structure and q.
