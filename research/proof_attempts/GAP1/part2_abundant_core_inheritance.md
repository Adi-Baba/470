# Step 2: M Abundant Implies N = Mq^a Pseudoperfect

## Goal

Prove: if M is odd and pseudoperfect, then N = Mq^a is pseudoperfect for any prime q ∤ M.

Combined with the base cases (k ≤ 3 handled by Paper 9), this closes Gap 1 for all k ≥ 4
where the M-core is itself abundant.

---

## Core Theorem

**Theorem 2.1 (Strong Inheritance):**  
Let M be a positive integer and q a prime with q ∤ M. If M is pseudoperfect, then Mq^a is pseudoperfect for all a ≥ 1.

---

## Proof by Induction on a

### Base Case: a = 1

M pseudoperfect ⟹ ∃ S_M ⊆ D(M) with Σ S_M = M.

Define T_M = D(M) \ S_M (complement in proper divisors of M).  
Then: Σ T_M = (σ(M) − M) − M = σ(M) − 2M = E(M).

**Construct T ⊆ D(Mq) as follows:**

```
T = { d : d | M }  ∪  { q · t : t ∈ T_M }
```

**Check T ⊆ D(Mq):**
- Every d | M satisfies d ≤ M < Mq, so d is a proper divisor of Mq. ✓  
- Every t ∈ T_M satisfies t < M (proper divisor), so q·t < qM = N. And q·t | qM. ✓  
- No element equals Mq. ✓

**Compute Σ T:**
```
Σ T = σ(M)  +  q · E(M)
     = σ(M)  +  q(σ(M) − 2M)
     = σ(M)(1 + q) − 2Mq
     = σ(Mq) − 2Mq        [since σ(Mq) = σ(M)·σ(q) = σ(M)(q+1)]
     = E(Mq)
```

By Lemma 0 (Complement Equivalence from Step 1): Σ T = E(Mq) implies Mq is pseudoperfect. ∎

---

### Inductive Step: a → a+1

**Induction hypothesis:** Mq^a is pseudoperfect (where M pseudoperfect, q ∤ M).

Let N_a = Mq^a and N_{a+1} = Mq^{a+1}.

Since N_a is pseudoperfect: ∃ T_a ⊆ D(N_a) with Σ T_a = E(N_a).

**Construct T_{a+1} ⊆ D(N_{a+1}) as follows:**

```
T_{a+1} = { d : d | N_a }  ∪  { q · t : t ∈ T_a }
```

**Check T_{a+1} ⊆ D(N_{a+1}):**
- Every d | N_a satisfies d ≤ N_a < qN_a = N_{a+1}. And d | N_{a+1}. ✓  
- Every t ∈ T_a is a proper divisor of N_a, so t < N_a. Then q·t < qN_a = N_{a+1}. And q·t | N_{a+1}. ✓

**Compute Σ T_{a+1}:**
```
Σ T_{a+1} = σ(N_a)  +  q · E(N_a)
```

Using excess recursion: E(N_{a+1}) = q · E(N_a) + σ(N_a).

So: **Σ T_{a+1} = E(N_{a+1})**. ✓

By Complement Equivalence: N_{a+1} = Mq^{a+1} is pseudoperfect. ∎

---

## The Induction Chain for k ≥ 4

We now have the full inductive argument across the number of prime factors:

**Theorem 2.2 (Complete Induction over k):**

*Base:* k = 3. As rigorously proven in the Gap 2 resolution (Divisor Descent), any odd abundant number with exactly 3 distinct prime factors is unconditionally pseudoperfect. ✓

*Step:* Assume every odd abundant number with exactly k−1 prime factors is pseudoperfect.  
Let N have k prime factors. Write N = Mq^a where q is the largest prime.  
Then M has k−1 prime factors.

**Case A: M is abundant.**  
By induction hypothesis, M is pseudoperfect.  
By Theorem 2.1, N = Mq^a is pseudoperfect. ✓

**Case B: M is deficient.**  
→ This is the remaining open case (Step 3).

---

## What Step 2 Closes

Step 2 definitively closes the case: **odd abundant N where the M-core is abundant**.

For this case, no computation is needed. The proof is purely algebraic:
1. Induction on the number of prime factors (base k=3 from Gap 2 resolution)
2. Inheritance of pseudoperfectness via the complement + scaling construction

The only remaining case for odd weird numbers is: N = Mq^a abundant, M deficient.

---

## Structural Constraint on Remaining Case

From Step 1 (Corollary 1.2), if M deficient and N = Mq^a abundant:

```
σ(M) > q^a · |E(M)|      ... (*)
```

For a = 1: σ(M) > q · |E(M)| = q(2M − σ(M))  
⟹ σ(M)(1 + q) > 2qM  
⟹ I(M) > 2q/(q+1)

For q = 11: I(M) > 22/12 = 11/6 ≈ 1.833  
For q = 13: I(M) > 26/14 = 13/7 ≈ 1.857  
For q → ∞: I(M) → 2

**So M must be "near-abundant": I(M) > 2q/(q+1), which approaches 2 as q grows.**

This severely restricts M. M must have high abundancy index despite being deficient.  
The structure of such near-abundant deficient odd numbers feeds directly into Step 3.
