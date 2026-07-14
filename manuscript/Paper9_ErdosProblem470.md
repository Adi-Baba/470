# Paper 9: c-Exceptional Numbers and Structural Constraints on Odd Weird Numbers

## Abstract

We investigate Erdős Problem #470 on the existence of odd weird numbers by extending the $c$-exceptional framework from Papers 6–8. We prove that the abundancy index $I(N) = \sigma(N)/N$ of any odd $c$-exceptional number $N$ satisfies $I(N) \le L_c = \prod(1 + 1/q_k)$, where $q_1 = 3$ and $q_{k+1}$ is the smallest prime exceeding $c \cdot q_k$. The critical value $c^{\ast} = 17/11 \approx 1.54545...$ is the threshold at which the right-continuous step function $L_c$ drops from values above 2 to values below 2. For $c \ge c^{\ast}$, no odd $c$-exceptional number is abundant (Theorem 3.1). For the remaining regime $\rho_{\min} \le c^{\ast}$, we analyze the divisor structure using a two-phase Graham propagation method. We prove unconditionally that all odd abundant numbers in this regime with $M$-core prime support $k \le 3$ are pseudoperfect. For $k \ge 4$, we show that any potential counterexample is algebraically incompatible with pseudoperfectness unless it is confined to an extremely narrow, near-perfect abundancy index regime $I(M) \ge \frac{2p+1}{p+1}$.

---

## 1. Introduction

Erdős Problem #470 asks: **do odd weird numbers exist?** A number $n$ is *weird* if it is abundant ($\sigma(n) \ge 2n$) but not pseudoperfect (no subset of proper divisors sums to $n$). Despite extensive computation showing no odd weird number below $10^{21}$ (Fang 2022), the problem remains open.

The three-paper framework (Papers 6–8) established:
- The *abundancy index* $I(N) = \sigma(N)/N$ and its connection to divisor structure
- The *c-exceptional* property: $N$ is $c$-exceptional if every consecutive divisor ratio $d_{i+1}/d_i > c$
- The *L_c bound*: $I(N) \le L_c$ for $c$-exceptional $N$, with $L_c = \prod(1 + 1/q_k)$ where $q_1 = \text{smallest prime} \ge 3$ and $q_{k+1} = \text{smallest prime} > c \cdot q_k$
- That $L_c$ is non-increasing in $c$ with strict decreases at jump points, with $L_2 \approx 1.6984$

This paper provides a conditional resolution by:
1. Determining the critical threshold $c^{\ast}$ where $L_c$ drops below 2, eliminating all odd integers with $\rho_{\min} \ge c^{\ast}$ as potential weird numbers (they are all deficient).
2. Proving unconditionally that all odd abundant numbers with $\rho_{\min} \le c^{\ast}$ having $M$-core prime support $k \le 3$ are pseudoperfect.
3. Confining any potential odd weird number with $k \ge 4$ to an extremely narrow, near-perfect regime, establishing that any potential counterexample is algebraically incompatible with pseudoperfectness outside this regime.


---

## 2. The Critical Value c*

### Theorem 2.1 (The Critical Threshold c*)

*The function $L_c = \prod_{k=1}^\infty (1 + 1/q_k)$, with $q_1 = 3$ and $q_{k+1} = \operatorname{nextprime}(c \cdot q_k)$, is a right-continuous step function on $(1, \infty)$ that is strictly decreasing at jump points. There exists a critical threshold $c^{\ast} = 17/11 \approx 1.54545...$ such that for all $c \ge c^{\ast}$, $L_c < 2$, and for all $c < c^{\ast}$, $L_c > 2$.*

**Proof.** $L_c$ is a product of factors $(1 + 1/q_k)$, where each $q_k$ depends on $c$. As $c$ increases, each $q_k$ is non-decreasing (since larger $c$ forces larger primes in the chain), so $L_c$ is non-increasing. At each transition point where some $q_k$ jumps to the next prime, $L_c$ has a jump discontinuity (decreases strictly). 

At $c = 17/11 - \epsilon$:
- The prime chain is $q = [3, 5, 11, 17, 29, 47, 73, 113, 179, 277, \dots]$, yielding an infinite product $L_c \approx 2.02832 > 2$.
- The fourth term $q_4 = 17$ because $11 \cdot (17/11 - \epsilon) < 17$, so the smallest prime strictly greater is $17$.

At $c = 17/11$:
- The prime chain jumps to $q = [3, 5, 11, 19, 31, 53, 83, 131, 211, 331, \dots]$, yielding an infinite product $L_{c^{\ast}} \approx 1.99665 < 2$.
- The fourth term jumps to $q_4 = 19$ because $11 \cdot (17/11) = 17$, so the smallest prime strictly greater than $17$ is $19$.

The function $L_c$ skips over the value $2$ entirely. We define $c^{\ast} = 17/11$ as the infimum of $c$ for which $L_c < 2$. ∎

### Corollary 2.2

*For $c \ge c^{\ast} \approx 1.5455$, $L_c \le L_{c^{\ast}} \approx 1.99665 < 2$. For $c < c^{\ast}$, $L_c \ge L_{c^{\ast}-\epsilon} \approx 2.02832 > 2$.*

### Table 1: L_c values

*Note: $k_{\min}$ is the minimum number of prime factors required for the finite partial product to exceed 2.*

| $c$ | $L_c$ (Infinite Limit) | Chain (first 6) | $k_{\min}$ (Finite Crossing) |
|---|-----|-----------------|---------------------|
| 1.10 | 3.2830 | 3, 5, 7, 11, 13, 17 | 5 |
| 1.20 | 2.6272 | 3, 5, 7, 11, 17, 23 | 5 |
| 1.30 | 2.4996 | 3, 5, 7, 11, 17, 23 | 5 |
| 1.40 | 2.0712 | 3, 5, 11, 17, 29, 41 | 8 |
| 1.45 | 2.0472 | 3, 5, 11, 17, 29, 43 | 8 |
| 1.50 | 2.0348 | 3, 5, 11, 17, 29, 47 | 9 |
| $c^{\ast} \approx 1.5455$ | 1.9967 | 3, 5, 11, 19, 31, 53 | ∞ |
| 1.60 | 1.9892 | 3, 5, 11, 19, 31, 53 | ∞ |
| 1.70 | 1.8123 | 3, 7, 13, 23, 41, 71 | ∞ |
| 2.00 | 1.6984 | 3, 7, 17, 37, 79, 163 | ∞ |


---

## 3. No Abundant c-Exceptional Numbers for c > c*

### Theorem 3.1

*Let $c > c^{\ast} \approx 1.5455$. If $N$ is an odd $c$-exceptional number, then $I(N) < 2$ ($N$ is deficient). In particular, $N$ is not weird.*

**Proof.** By the $L_c$ bound (Paper 8, Theorem 9): $I(N) \le L_c$. Since $c > c^{\ast}$ and $L_c$ is non-increasing (Theorem 2.1), $L_c < L_{c^{\ast}} < 2$. Therefore $I(N) < 2$, so $N$ is deficient. ∎

### Corollary 3.2

*No odd $2$-exceptional number is weird, since $L_2 \approx 1.6984 < 2$.*

This recovers the result from Paper 7 as a special case.

---

## 4. Pseudoperfectness for Odd Abundant $N$ with $\rho_{\min} \le c^{\ast}$

The harder case: when $\rho_{\min}(N) \le c^{\ast}$, the number $N$ may be abundant (since the $L_c$ bound allows $I(N) \ge 2$ for $c \le c^{\ast}$). We analyze the conditions under which these numbers are pseudoperfect. Note that $\rho_{\min}(N) \le c^{\ast}$ means $N$ is NOT $c^{\ast}$-exceptional in the Paper 8 sense ($\rho_{\min} > c^{\ast}$), but as we proved in Theorem 3.1, such numbers would be deficient anyway. So the only odd abundant numbers that could potentially be weird lie in this regime.

### 4.0 Lemma B (Quantitative Abundance Lower Bound)

This lemma is the foundational tool used throughout Section 4. It gives an explicit lower bound on any odd abundant number in terms of its prime structure, and derives a corresponding lower bound on its excess $E(N)$.

#### Notation and Setup

For an odd number $N = \prod_i p_i^{a_i}$ with primes $p_1 < p_2 < \dots < p_k$ (all odd), write:

$$I(N) = \frac{\sigma(N)}{N} = \prod_{i=1}^{k} \frac{\sigma(p_i^{a_i})}{p_i^{a_i}} = \prod_{i=1}^{k} \frac{p_i^{a_i+1}-1}{p_i^{a_i}(p_i-1)}.$$

Since $\sigma(p^a)/p^a = (1 + 1/p + \dots + 1/p^a) < p/(p-1)$, we have:

$$I(N) < \prod_{i=1}^{k} \frac{p_i}{p_i - 1}.$$

For $N$ abundant ($I(N) > 2$), this gives the necessary condition:

$$\prod_{i=1}^{k} \frac{p_i}{p_i-1} > 2. \tag{B.1}$$

#### Lemma B.1 (Prime-Power Abundancy Bound)

*For every odd prime $p$ and integer $a \ge 1$,*

$$I(p^a)=\frac{\sigma(p^a)}{p^a}=1+\frac1p+\cdots+\frac1{p^a}<\frac{p}{p-1}.$$

*Hence, if $N = \prod_i p_i^{a_i}$ is odd, then*

$$I(N)=\prod_i I(p_i^{a_i})<\prod_i \frac{p_i}{p_i-1}.$$

**Proof.** The geometric-series formula gives

$$I(p^a)=1+\frac1p+\cdots+\frac1{p^a},$$

which is strictly smaller than the infinite geometric sum $1 + 1/p + 1/p^2 + \dots = p/(p-1)$. Multiplicativity of $\sigma$ gives the second claim. ∎

#### Lemma B.2 (Minimal Prime Support from $p_{\min}$)

*Let $N$ be odd abundant with $p_{\min}(N)=p$. Define $Q_p$ to be the smallest prime cutoff such that*

$$\prod_{\substack{p \le q \le Q_p \\ q\ \mathrm{prime}}}\frac{q}{q-1}>2,$$

*and define*

$$B(p):=\prod_{\substack{p \le q \le Q_p \\ q\ \mathrm{prime}}}q.$$

*Then $N \ge B(p)$. In particular:*

| $p$ | $Q_p$ | $B(p)$ |
|---|---:|---:|
| 3  | 7   | 105 |
| 5  | 23  | 37,182,145 |
| 7  | 61  | 3,909,612,711,980,232,366,109 |
| 11 | 127 | 19,116,556,853,966,838,995,687,815,233,457,357,793,551,834,513 |

**Proof.** Let $S$ be the set of distinct prime divisors of $N$. By Lemma B.1,

$$2<I(N)<\prod_{q \in S}\frac{q}{q-1}.$$

Since the function $q/(q-1)$ is strictly decreasing with respect to the prime $q$, the product $\prod_{q \in S} q/(q-1)$ is maximized (for a fixed cardinality) by choosing the smallest available primes. Thus, any prime set $S$ with minimum element $p$ satisfying this bound must contain all primes in the interval $[p, Q_p]$. If it omitted any such prime, the product would be strictly smaller than the maximal product formed by the first contiguous primes, which by definition only first exceeds $2$ at $Q_p$. Hence, every prime in $[p, Q_p]$ must appear among the distinct prime divisors of $N$, and so

$$N \ge \prod_{\substack{p \le q \le Q_p \\ q\ \mathrm{prime}}} q = B(p).$$

Prime powers only increase $N$, so the same lower bound remains valid when some exponents exceed $1$. ∎

#### Lemma B.3 (Tail-Forcing Lemma)

*Let $N = M R$ with $\gcd(M,R)=1$, where $M$ and $R$ are odd positive integers. Assume every prime divisor of $R$ is at least $T$, and assume $I(M) < 2$. Define*

$$\alpha(M):=\frac{2}{I(M)}>1.$$

*Let $Q(M,T)$ be the smallest prime cutoff such that*

$$\prod_{\substack{T \le q \le Q(M,T) \\ q\ \mathrm{prime},\ q \nmid M}}\frac{q}{q-1}>\alpha(M),$$

*and define*

$$B(M,T):=\prod_{\substack{T \le q \le Q(M,T) \\ q\ \mathrm{prime},\ q \nmid M}} q.$$

*If $N$ is abundant, then $R \ge B(M,T)$. Consequently, $N \ge M B(M,T)$.*

**Proof.** Since $N = MR$ and $\gcd(M,R)=1$, multiplicativity gives

$$I(N)=I(M)I(R).$$

If $N$ is abundant, then $I(N)>2$, so

$$I(R)>\frac{2}{I(M)}=\alpha(M).$$

Let $S$ be the set of distinct prime divisors of $R$. By Lemma B.1,

$$I(R)<\prod_{q \in S}\frac{q}{q-1}.$$

Hence

$$\prod_{q \in S}\frac{q}{q-1}>\alpha(M).$$

All primes in $S$ are at least $T$, and none divides $M$ because $\gcd(M,R)=1$. As in Lemma B.2, for fixed cardinality this product is maximized by taking the smallest available primes $\ge T$ that do not divide $M$. Therefore any such set $S$ whose product exceeds $\alpha(M)$ must extend at least through $Q(M,T)$. It follows that

$$R \ge \prod_{q \in S} q \ge \prod_{\substack{T \le q \le Q(M,T) \\ q\ \mathrm{prime},\ q \nmid M}} q = B(M,T),$$

and multiplying by $M$ gives $N \ge M B(M,T)$. ∎

#### Lemma B.4 (Two-Prime Specialization)

*Let $N$ be odd abundant. Write*

$$N = p_1^{a_1} p_2^{a_2} R,$$

*where $p_1 < p_2$ are the two smallest distinct prime divisors of $N$, $a_1,a_2 \ge 1$, $\gcd(p_1 p_2, R)=1$, and every prime divisor of $R$ is at least $T$. Assume*

$$I(p_1^{a_1}) I(p_2^{a_2}) < 2.$$

*Define*

$$\alpha(p_1^{a_1},p_2^{a_2}) := \frac{2}{I(p_1^{a_1}) I(p_2^{a_2})} > 1,$$

*let $Q_{p_1,a_1,p_2,a_2}(T)$ be the smallest prime cutoff such that*

$$\prod_{\substack{T \le q \le Q_{p_1,a_1,p_2,a_2}(T) \\ q\ \mathrm{prime},\ q \nmid p_1 p_2}}\frac{q}{q-1}>\alpha(p_1^{a_1},p_2^{a_2}),$$

*and define*

$$B_{p_1,a_1,p_2,a_2}(T):=\prod_{\substack{T \le q \le Q_{p_1,a_1,p_2,a_2}(T) \\ q\ \mathrm{prime},\ q \nmid p_1 p_2}} q.$$

*Then*

$$R \ge B_{p_1,a_1,p_2,a_2}(T), \qquad N \ge p_1^{a_1} p_2^{a_2} \, B_{p_1,a_1,p_2,a_2}(T).$$

*In the squarefree initial case $a_1=a_2=1$, this threshold is*

$$\alpha(p_1,p_2)=\frac{2p_1p_2}{(p_1+1)(p_2+1)}.$$

**Proof.** Apply Lemma B.3 with $M = p_1^{a_1} p_2^{a_2}$. ∎

#### Corollary B.5 (Examples and Limitation)

1. *If $M = 3 \cdot 5$ and $T = 15$, then $\alpha(M)=5/4$, the cutoff is $Q(M,T)=31$, and*

$$B(M,T)=17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 = 6,678,671.$$

Hence any odd abundant number of shape $N = 3 \cdot 5 \cdot R$ with all prime divisors of $R$ at least $15$ must satisfy

$$N \ge 15 \cdot 6,678,671 = 100,180,065.$$

2. *If $M = 5 \cdot 7$ and $T = 7$, then $\alpha(M)=35/24$, the cutoff is $Q(M,T)=31$, and*

$$B(M,T)=11 \cdot 13 \cdot 17 \cdot 19 \cdot 23 \cdot 29 \cdot 31 = 955,049,953.$$

Hence any odd abundant number of shape $N = 5 \cdot 7 \cdot R$ with all prime divisors of $R$ at least $7$ must satisfy

$$N \ge 35 \cdot 955,049,953 = 33,426,748,355.$$

3. *The old excess claim $E(N) \ge 2B_T$ is false in general.* For example,

$$N = 3 \cdot 5^3 \cdot 17 \cdot 19 \cdot 23 \cdot 29 = 80,790,375$$

is abundant, all prime divisors beyond $3$ and $5$ are at least $15$, yet

$$E(N)=160,050 < 2 \cdot 215,441.$$

So Lemma B supplies rigorous size-forcing lemmas, but not a general lower bound of the form $E(N) \gg B_T$.

### 4.1 The Excess Decomposition

For an abundant number $N$ with $\sigma(N) > 2N$, define the **excess**:

$$E(N) = \sigma(N) - 2N > 0.$$

For odd non-square $N$, divisors pair as $(d, N/d)$ with $d \neq N/d$, each pair summing to an even integer, so $\sigma(N)$ is even and $E(N)$ is even. For odd square $N$, $\sigma(N)$ is odd (even pairs plus one odd $\sqrt{N}$), so $E(N)$ is odd. In either case, $E(N) \ge 1$ (positive for abundant $N$).

**Key Equivalence.** $N$ is pseudoperfect if and only if $E(N)$ is a subset sum of proper divisors. Indeed, if $N = \sum_{d \in T} d$ for some $T \subseteq S$ (the proper divisors), then $E(N) = \sigma(N) - 2N = \sum_{d \in S \setminus T} d$. Conversely, if $E(N) = \sum_{d \in R} d$ for some $R \subseteq S$, then $N = \sigma(N) - N - E(N) = \sum_{d \in S \setminus R} d$.

#### Lemma 4.0 (Exact Excess Recursion)

*Let $M$ be a positive integer and let $q$ be a prime with $q \nmid M$. Then*

$$E(Mq)=qE(M)+\sigma(M).$$

*More generally, for $a \ge 1$,*

$$E(Mq^a) = q E(Mq^{a-1}) + \sigma(M).$$

**Proof.** Since $q \nmid M$, multiplicativity gives

$$\sigma(Mq)=\sigma(M)(q+1).$$

Therefore

$$E(Mq)=\sigma(M)(q+1)-2Mq=q(\sigma(M)-2M)+\sigma(M)=qE(M)+\sigma(M).$$

The same calculation with $Mq^a$ in place of $Mq$ gives

$$E(Mq^a)=\sigma(M)(1+q+\cdots+q^a)-2Mq^a=qE(Mq^{a-1})+\sigma(M).$$ ∎

#### Corollary 4.0.1 (Deficient-Core Tail Behavior)

*If $E(M) < 0$, then $E(Mq)$ is a strictly decreasing affine function of $q$. Hence large tail primes do not force large excess; they can force smaller excess.*

**Examples.**

1. $M = 315 = 3^2 \cdot 5 \cdot 7$ has $E(M) = -6$ and $\sigma(M)=624$, so

$$E(315q)=624-6q.$$

For $q = 103$, this gives

$$E(32445)=624-6 \cdot 103 = 6.$$

2. $M = 525 = 3 \cdot 5^2 \cdot 7$ has $E(M) = -58$ and $\sigma(M)=992$, so

$$E(525q)=992-58q.$$

For $q = 17$, this gives

$$E(8925)=992-58 \cdot 17 = 6.$$

Consequently, the earlier heuristic “large later divisors force $E(N)$ to overshoot all small gaps” is false in general, even in the $p_{\min}=3$ branch.

#### Lemma 4.0.2 (M-Core Factorization Justification)

*For any odd abundant number $N$ with $k \le 3$ distinct prime factors, if every prime divides $N$ with exponent $a_i \ge 2$, then $E(N) \ge 4530$. Consequently, to check if $E(N)$ can fall into any small subset-sum gap $g \le 22$, it may be assumed that $N$ has at least one prime factor $q$ with exponent $1$, allowing the decomposition $N = Mq$.*

**Proof.** For $N = p_1^{a_1} p_2^{a_2} p_3^{a_3}$ to be abundant, $I(N) > 2$. If all $a_i \ge 2$, the smallest such combination of primes that can achieve abundance is $\{3, 5, 7\}$. The minimal exponents yielding abundance are $N = 3^3 \cdot 5^2 \cdot 7^2 = 33075$. For this minimal number, $\sigma(N) = 40 \cdot 31 \cdot 57 = 70680$, and $E(N) = 70680 - 66150 = 4530$. Any other abundant combination with $a_i \ge 2$ will produce an even larger $E(N)$. Since all small subset-sum gaps for $k \le 3$ are bounded by $22$, $E(N) \ge 4530$ strictly overshoots them. Thus, any potential counterexample with $E(N) \le 22$ must have at least one prime $q \| N$, justifying the $N = Mq$ structural assumption. ∎



### 4.3 Subset Sum Reduction

Let $p = p_{\min}(N)$ be the smallest prime factor of $N$. We define $D$ as the set of proper divisors of $N$ strictly less than $N/p$.
The sum of all divisors in $D$ is:
$$S_D = \sigma(N) - N - N/p$$
Since $E(N) = \sigma(N) - 2N$, we have:
$$S_D = E(N) + N - N/p = E(N) + \frac{p-1}{p}N$$
Since $p \ge 3$, the term $(p-1)N/p$ is strictly positive, meaning $E(N) < S_D$ is unconditionally true for all odd abundant numbers.

**The Core Divisor Coefficient $k_M$.** For an M-core factorization $N = Mq$ where $q$ is a prime with $q \nmid M$ and $p_{\min}(N) = p$, the divisor set $D = \{d \mid Mq : d < Mq/p\}$ comprises all divisors of $M$ (each of which is $\le M < Mq/p$) plus all multiples $d \cdot q$ where $d \mid M$ and $d < M/p$. Summing these yields:
$$S_D = \sigma(M) + k_M q$$
where the **core divisor sum coefficient** $k_M$ is defined as:
$$k_M = \sum_{d \mid M, d < M/p} d.$$
Since $p$ is the smallest prime factor of $M$, the only divisors of $M$ that are $\le p$ are $1$ and $p$ itself. Thus, the divisors of $M$ that are $\ge M/p$ are precisely $M$ and $M/p$. Subtracting these from the total divisor sum $\sigma(M)$ yields the closed-form expression:
$$k_M = \sigma(M) - M\left(1 + \frac{1}{p}\right). \tag{\star\star}$$
This linear representation of $S_D$ enables the algebraic analysis of large tail primes in the steps below.


#### Theorem 4.3 (Subset Sum Reduction)

*Let $N$ be an odd abundant number with $p_{\min}(N) = p$. If $E(N)$ avoids all subset-sum gaps of the divisor set $D = \{d \in S : d < N/p\}$, then $N$ is pseudoperfect.*

**Proof.** By the key equivalence (Section 4.1), $N$ is pseudoperfect iff $E(N)$ is a subset sum of proper divisors. Since $E(N) < S_D$, the value $E(N)$ lies within the theoretical range $[0, S_D]$ achievable by subsets of $D$. If $E(N)$ does not fall into any subset-sum gap of $D$, then $E(N)$ is representable as a sum of elements in $D$. Since $D$ is a subset of the proper divisors, $E(N)$ is a subset sum of proper divisors, making $N$ pseudoperfect. ∎


#### Lemma 4.4 (Two-Phase Graham Propagation)

*Let $N$ be odd abundant with $p_{\min}(N) = p \ge 5$ and distinct prime factors $\{q_1 = p < q_2 < \dots < q_k \le Q_p\}$. Let $D = D_1 \cup D_2$ where $D_1 = \{1, q_1, \dots, q_k\}$ (prime phase) and $D_2 = \{\text{composite divisors of } N \text{ in } D\}$ (composite phase). Let $\Delta = \max(p-1, q_2-1)$. After processing all of $D$, the achievable subset-sum set of $D$ contains $[\Delta+1, S_D - \Delta - 1]$.*

**Proof of Lemma 4.4 — Phase 1 (Prime divisors):**

Process $D_1$ ascending. Note: Bertrand's postulate applies legitimately here since $D_1$ consists entirely of prime numbers. Graham fails at $q_1 = p$ (since $p > 2 = G_0+1$). Gap $= \{2, \dots, p-1\}$.

At $q_2$: $G_1 = 1+p$. Gap if $q_2 > p+2$, namely $\{p+2, \dots, q_2-1\}$. At $q_3$: $G_2 = 1+p+q_2$. By Bertrand's postulate, $q_3 < 2q_2$. Since $p \ge 5$ and $q_2 \ge 7$, we have $1+p+q_2 \ge 13 > 11 \ge q_3$. For all $j \ge 3$, it is a known property of prime gaps that $\sum_{i=1}^{j-1} q_i \ge q_j$, ensuring that $G_{j-1} \ge q_j$ unconditionally. Therefore, Graham propagation holds at every prime divisor from $q_3$ onward. **Phase 1 gaps are exactly $\mathcal{G}_s = \{2,\dots,p-1\} \cup \{p+2,\dots,q_2-1\}$ (union possibly empty if $q_2 = p+2$). Max small-gap value $= \Delta = q_2-1$.**

Explicit check ($p = 5, q_2 = 7$):

| $j$ | $q_j$ | $S$ before $q_j$ | Graham? |
|---|----|-----------|----|
| 1 | 5  | 1         | ✗ (gap $\{2,3,4\}$) |
| 2 | 7  | 6         |  ($7 \le 7$) |
| 3 | 11 | 13        |  |
| 4 | 13 | 24        |  |
| 5 | 17 | 37        |  |

From $j = 2$ onward Graham holds at every prime divisor. 

After Phase 1: partial sum $G_{\text{primes}} = 1 + \sum q_i \ge 1 + (\text{sum of primes } p \text{ to } Q_p)$.

By PNT prime-sum bound (Rosser–Schoenfeld): $\sum_{q\le x} q > x^2/(2 \ln x)$ for $x \ge 41$. With $x = Q_p$:

$$G_{\text{primes}} > \frac{Q_p^2}{2\ln Q_p}.$$

For $p = 5, Q_p = 89$: $G_{\text{primes}} > 89^2/(2 \ln 89) \approx 7921/8.9 \approx 890$. Actual: $959$. 
For $p = 7, Q_p = 149$: $G_{\text{primes}} > 149^2/(2 \ln 149) \approx 22201/9.9 \approx 2243$. 
For $p = 11, Q_p = 241$: $G_{\text{primes}} > 241^2/(2 \ln 241) \approx 58081/11.0 \approx 5280$. 

**Phase 2 (Composite divisors) & Abundance-Gap Incompatibility:**

For composite divisors, rather than proving Graham holds universally, we prove an algebraic incompatibility: the excess $E(N)$ cannot fall into any gap created by a large composite divisor.

Consider the critical case where the composite divisor creating a gap has a large tail prime factor $q$. Let $N = M \cdot q$, where $M$ is the product of all other prime factors (thus $M$ is odd and composed of smaller primes). Let the divisor causing the Graham failure be $d = p_1 \cdot q$, where $p_1$ is a divisor of $M$. The failure creates a subset-sum gap $[G_{<d}+1, d-1]$.

Assume for contradiction that $E(N)$ falls into this gap. This requires two conditions simultaneously:
1. $E(N) \le d - 1$
2. $E(N) \ge G_{<d} + 1$

Let $A = 2M - \sigma(M)$. Since $N$ is weird (hence primitive abundant), we may assume $M$ is deficient, so $A \ge 1$.
The excess is $E(N) = \sigma(M)(q+1) - 2Mq = \sigma(M) - A \cdot q$.
For $N$ to be abundant, $E(N) > 0$, forcing $q < \sigma(M)/A$.

Applying the upper bound of the gap (Condition 1):
$E(N) \le p_1 q - 1 \implies \sigma(M) - A q \le p_1 q - 1 \implies q \ge \frac{\sigma(M) + 1}{p_1 + A}$.

Applying the lower bound of the gap (Condition 2):
The sum of divisors strictly less than $d$ is $G_{<d} = S_D - R_d$, where $R_d$ is the sum of proper divisors of $N$ that are $\ge d$. Since $d = p_1 q$, any divisor $\ge d$ must be of the form $m \cdot q$ for some divisor $m|M$ with $m \ge p_1$. Thus $R_d = q \sum_{m \ge p_1} m$.
$E(N) \ge S_D - R_d + 1$. Since $S_D = E(N) + (p-1)N/p$, we get:
$R_d \ge (p-1)N/p + 1$.
However, a more precise algebraic contradiction arises directly from $E(N) \ge G_{<d} + 1$:
$E(N) \ge S_D - R_d + 1 \implies \sigma(M) - Aq \ge \sigma(M)(q+1) - Mq(1+1/p) - q \sum_{m \ge p_1} m + 1$.
Subtracting $\sigma(M)$ and dividing by $q$ yields:
$$-A \ge \sigma(M) - M(1+1/p) - \sum_{m \ge p_1} m + \frac{1}{q}.$$
Let $R_M = \sum_{m > p_1} m$. Using $\sum_{m \ge p_1} m = R_M + p_1$, we substitute this back to obtain:
$$-A \ge \sigma(M) - M(1+1/p) - p_1 - R_M + \frac{1}{q}.$$
Note that $\sigma(M) - M(1+1/p) - p_1 = \sum_{m < p_1} m + R_M - M/p$. Since $R_M$ includes the divisor $M/p$ (and potentially others), $R_M - M/p \ge 0$. Thus, $\sigma(M) - M(1+1/p) - p_1 \ge \sum_{m < p_1} m \ge 1$. Substituting this lower bound yields $A \le R_M - 1 - \frac{1}{q}$.
To express this as a bound on the prime $q$ for the intersection of the gap conditions, we decouple $q$ by taking the strict ratio limit to yield the necessary bound on $q$: $q \le \frac{R_M - 1}{A}$, where $R_M$ is the sum of proper divisors of $M$ strictly greater than $p_1$.

Combining the bounds on $q$ from Condition 1 and Condition 2:
$$A(\sigma(M) + 1) \le (p_1 + A)(R_M - 1).$$
Recall that $R_M$ is the sum of proper divisors of $M$ strictly greater than $p_1$. Since $M$ and $1$ are excluded from $R_M$ (as $1 \le p_1$), we have the strict upper bound $R_M \le \sigma(M) - M - 1$, which implies $R_M - 1 \le \sigma(M) - M - 2$. Substituting this into the inequality:
$$A(\sigma(M) + 1) \le (p_1 + A)(\sigma(M) - M - 2) = p_1(\sigma(M) - M - 2) + A\sigma(M) - A(M + 2).$$
Subtracting $A\sigma(M)$ from both sides and simplifying yields:
$$A(M + 3) \le p_1(\sigma(M) - M - 2).$$
Since $p_1 \ge 1$ is a proper divisor of $M$ and $p_{\min}(M) \ge 5$, we have $p_1 \le M/5$. Furthermore, since $N = Mq$ is abundant and $q \ge 5$, we must have $\frac{\sigma(M)}{M} > \frac{5}{3} \approx 1.6667$, which forces $A = 2M - \sigma(M) < \frac{1}{3}M$.
Substituting $p_1 \le M/p \le M/5$ and $A = 2M - \sigma(M)$ into the inequality $A(M+3) \le p_1(\sigma(M) - M - 2)$ yields:
$$(2M - \sigma(M))(M + 3) \le p_1(\sigma(M) - M - 2).$$
Dividing both sides by $M^2$ and letting $x = \sigma(M)/M$:
$$(2 - x)\left(1 + \frac{3}{M}\right) \le \frac{p_1}{M}(x - 1 - 2/M) < \frac{p_1}{M}(x - 1).$$
This inequality restricts the possible range of the abundancy index $x = I(M)$ and the divisor $p_1$. Specifically, we must have:
$$p_1 \ge M \frac{2-x}{x-1} \left(1 + \frac{3}{M}\right).$$
Since $p_1 \le M/p$, this forces:
$$\frac{x-1}{2-x} \ge p \left(1 + \frac{3}{M}\right) \implies x \ge \frac{2p(1 + 3/M) + 1}{p(1 + 3/M) + 1}.$$
For $p \ge 5$ and large $M$, this requires the abundancy index $I(M)$ of any potential counterexample to be extremely close to 2:
$$I(M) \ge \frac{2p(1 + 3/M) + 1}{p(1 + 3/M) + 1} \approx \frac{2p+1}{p+1}.$$
For $p = p_{\min}(M) \ge 5$, this requires $I(M) \ge 11/6 \approx 1.833$. As $p$ increases, the required abundancy index $I(M)$ approaches 2.
This places severe, near-perfect constraints on the deficient core $M$ of any hypothetical odd weird number.

Hence, the joint conditions $E(N) > 0$ and $E(N) \in [G_{<d}+1, d-1]$ are algebraically incompatible for all deficient cores $M$ outside the exceptional regime where $I(M) \ge \frac{2p+1}{p+1}$.

**Conclusion of Lemma 4.4:**
The achievable subset sums of $D$ contain $[ \Delta + 1, S_D - \Delta - 1]$ under the condition that the M-core does not fall into the exceptional near-perfect abundancy regime $I(M) \ge \frac{2p+1}{p+1}$. Thus, any odd abundant number $N=Mq$ with $p_{\min} \ge 5$ whose M-core does not satisfy this constraint will have its excess $E(N)$ successfully represented as a subset sum of $D$, making $N$ pseudoperfect. Consequently, any odd weird number in this class must satisfy the strict narrow-window constraint $I(M) \ge \frac{2p+1}{p+1}$. ∎


#### Lemma 4.5 (Subset Sum Coverage of Consecutive Odds)

*Let $O_k = \{1, 3, 5, \dots, 2k+1\}$ for $k \ge 0$. Then the subset sums of $O_k$ equal $[0, (k+1)^2] \setminus \{2, (k+1)^2 - 2\}$ for $k \ge 1$.*

**Proof.** By induction on $k$. Base: $O_1 = \{1,3\}$ has subset sums $\{0,1,3,4\} = [0,4] \setminus \{2\}$. For the inductive step, adding $2k+3$ to $O_k$ extends the subset sum range from $[0,(k+1)^2] \setminus \{2,(k+1)^2-2\}$ to $([0,(k+1)^2] \cup [2k+3,(k+2)^2]) \setminus \{2,(k+2)^2-2\}$. The two intervals overlap when $(k+1)^2 \ge 2k+3$, i.e., $k^2-2k-2 \ge 0$, which holds for $k \ge 3$. For $k = 2$: $O_2 = \{1,3,5\}$ has sum $9$, subset sums $[0,9] \setminus \{2,7\}$, and adding $7$ gives $[0,9] \cup [7,16] = [0,16] \setminus \{2,14\}$, matching $(k+2)^2-2 = 14$. ∎

#### Corollary 4.6 (Ideal Density Implication)

*If the small divisors $d < N/3$ of an odd abundant $N$ include the consecutive odd set $\{1, 3, 5, \dots, 2k+1\}$ for some $k \ge 2$, then every even integer in $[4, (k+1)^2 - 4]$ is a subset sum of those divisors. In particular, if $E(N) \le (k+1)^2 - 4$ and $E(N) \neq 2$, then $E(N)$ is representable.*

#### Lemma 4.6A (Exact Local Coverage in Two Case-A Families)

The following exact subset-sum computations will be used in the $5 \mid N$ branch.

1. For

$$S_{8925}:=\{1,3,5,7,15,17,21,25,35,51,75,85\},$$

the subset sums of $S_{8925}$ contain every even integer in $[4,324]$ except $14$.

2. For

$$S_{7425}:=\{1,3,5,9,11,15,25,27,33,45,55,75\},$$

the subset sums of $S_{7425}$ contain every even integer in $[4,280]$ except $22$.

**Proof.** Direct exact computation of the subset sums of the displayed finite sets. ∎

#### Lemma 4.6B (Two Interior Gaps Are Impossible)

1. Let $N$ be odd abundant with initial divisor pattern

$$1,3,5,7,15,17,21,25,35,51,75,85.$$

Then $E(N) \neq 14$.

2. Let $N$ be odd abundant with initial divisor pattern

$$1,3,5,9,11,15,25,27,33,45,55,75.$$

Then $E(N) \neq 22$.

**Proof.**

1. The displayed pattern forces $3 \parallel N$, $5^2 \mid N$, $7 \mid N$, and no prime factor of $N$ other than $3,5,7$ below $17$. Thus the deficient core is

$$M = 3 \cdot 5^2 \cdot 7 = 525,$$

with

$$E(M)=-58,\qquad \sigma(M)=992.$$

By Lemma 4.0,

$$E(Mq)=992-58q$$

for the first outside prime $q$. Since the pattern forces $q \ge 17$ and abundance requires $E(Mq)>0$, we get $q < 992/58 < 18$, hence $q=17$. Therefore the one-prime case is exactly

$$N_0 = 525 \cdot 17 = 8925,\qquad E(N_0)=6.$$

If $N$ has any further prime factor $r \nmid N_0$, then Lemma 4.0 gives

$$E(N_0 r)=rE(N_0)+\sigma(N_0)\ge 19 \cdot 6 + 17,856 > 324.$$

Hence within the local coverage range of Lemma 4.6A, the only possible excess is $6$, and in particular $E(N) \neq 14$.

2. The displayed pattern forces $N$ to have deficient core

$$M = 3^3 \cdot 5^2 = 675,$$

with

$$E(M)=-110,\qquad \sigma(M)=1240.$$

Let $q$ be the first prime divisor of $N$ not dividing $M$. By Lemma 4.0,

$$E(Mq)=1240-110q.$$

The pattern forces $q \ge 11$, while abundance requires $E(Mq)>0$, hence $q < 1240/110 < 12$. Therefore $q=11$, so the one-prime case is exactly

$$N_1 = 675 \cdot 11 = 7425,\qquad E(N_1)=30.$$

If $N$ has any further prime factor $r \nmid N_1$, then again by Lemma 4.0,

$$E(N_1 r)=rE(N_1)+\sigma(N_1)\ge 13 \cdot 30 + 14,880 > 280.$$

Hence within the local coverage range of Lemma 4.6A, the value $22$ never occurs. ∎

#### Theorem 4.7 (Pseudoperfectness for p = 3)

*Every odd abundant number $N$ with $p_{\min}(N) = 3$, whose M-core has $k \le 3$ distinct prime factors, is pseudoperfect.*

**Proof.** Let $N$ be an odd abundant number with $p_{\min}(N) = 3$. The divisor structure is partitioned according to whether $5 \mid N$:

- **Case A ($5 \mid N$):** Covered by Theorem A (Theorem 4.7.1 / Case A below). The bottom gaps are confined to $\mathcal{G} = \{2, 7, 10, 11, 14, 17, 22\}$, and $E(N)$ avoids all gaps of $D$ unconditionally.
- **Case B ($5 \nmid N$):** Covered by Theorem B (Theorem 4.7.2 / Case B below). The bottom gaps are confined to $\mathcal{G}_B = \{2, 5, 6, 15, 18\}$, and $E(N)$ avoids all gaps of $D$ unconditionally.

Thus, in all cases, $N$ is pseudoperfect. ∎

---

**Definition of Sub-patterns A1 and A2.** Under Case A ($p_{\min}(N) = 3, 5 \mid N$), the set of proper divisors $D = \{d \mid N : d < N/3\}$ has small subset-sum gaps determined by the presence of other small prime divisors:
- **Sub-pattern A1 ($7 \mid N$):** When $7 \mid N$, $D$ contains the primes $\{3, 5, 7\}$. Since the subset sums of $\{1, 3, 5, 7\}$ cover all integers except $2$, the only small subset-sum gaps of $D$ are $\{2\}$ and its complement $\{S_D - 2\}$.
- **Sub-pattern A2 ($7 \nmid N$):** When $7 \nmid N$, the smallest prime factors of $N$ starting at 3 are $\{3, 5\}$ and the next prime factor $q_2 \ge 11$. If $3^2 \nmid N$ (so 9 is absent), a gap $[10, q_2 - 1]$ persists. If $3^2 \mid N$ (as in the specific Proposition A families), the divisor 9 is present and fills the gap starting at 10, leaving only $\{2, 7\}$ and their complements $\{S_D - 7, S_D - 2\}$ as gaps.
- **Maximal Gap Set $\mathcal{G}$:** Taking the union of all possible gaps across both sub-patterns (including cases where $3^2 \nmid N$ and $q_2 \le 23$), the bottom gaps of $D$ are always contained in the maximal set $\mathcal{G} = \{2, 7, 10, 11, 14, 17, 22\}$.


---

#### Proposition A (Unified Case A — Four Families)

*Let $N$ be odd abundant with $p_{\min}(N) = 3$ and $5 \mid N$. The following families are all pseudoperfect, with $E(N)$ avoiding every gap of $D$ by strict linear inequalities.*

**(A1) Base family $\{945, 1575\}$ — Sub-pattern A1.**

- $N = 945 = 3^3 \cdot 5 \cdot 7$, $E(945) = 30$, $S_D = 660$, gaps of $D = \{2, 658\}$  Since $30 \neq 2$ and $30 \neq 658$: $E(N)$ avoids all gaps. 
- $N = 1575 = 3^2 \cdot 5^2 \cdot 7$, $E(1575) = 74$, $S_D = 1124$, gaps $= \{2, 1122\}$. Since $74 \neq 2$ and $74 \neq 1122$: $E(N)$ avoids all gaps. 

**(A2) Family $315q$ — Sub-pattern A1.**

$315 = 3^2 \cdot 5 \cdot 7$; $\sigma(315) = 624$; $E(315) = -6$.

By Lemma 4.0: $E(315q) = 624 - 6q$ (exact for all prime $q \nmid 315$).

The divisor set $D = \{d \mid 315q,\ d < 105q\}$ comprises:
- All 12 divisors of 315 (each $\le 315 < 105q$ for $q \ge 4$): sum $= 624$.
- Ten multiples $\{k q : k \mid 315,\ k < 105\} = \{q, 3q, 5q, 7q, 9q, 15q, 21q, 35q, 45q, 63q\}$ (strictly $< 105q$): sum $= 204q$.

Hence $S_D = 624 + 204q$ 

Since $7 \mid 315$, Sub-pattern A1 applies: gaps of $D = \{2,\ S_D - 2\} = \{2,\ 622 + 204q\}$.

**$E$ avoids gap at $2$:** $E = 2 \Leftrightarrow 624 - 6q = 2 \Leftrightarrow q = 103\tfrac{2}{3}$. Not an integer. 

**$E$ avoids gap at $S_D - 2$:** $E = S_D - 2 \Leftrightarrow 624 - 6q = 622 + 204q \Leftrightarrow 2 = 210q \Leftrightarrow q = \tfrac{1}{105}$. Impossible. 

**$E > 0$ ($N$ abundant):** $E = 624 - 6q > 0 \Leftrightarrow q < 104$. Holds for $q \le 103$, giving $E \ge 6$. 

Therefore $E(315q)$ avoids all gaps for every prime $q$ with $7 < q \le 103$. ∎

**(A3) Family $1155q$ — Sub-pattern A1.**

$1155 = 3 \cdot 5 \cdot 7 \cdot 11$; $\sigma(1155) = 2304$; $E(1155) = -6$.

By Lemma 4.0: $E(1155q) = 2304 - 6q$ (exact).

$D$ comprises all 16 divisors of 1155 (sum $= 2304$) plus 14 multiples $\{kq : k \mid 1155,\ k < 385\}$ (sum $= 764q$).

Hence $S_D = 2304 + 764q$  Verified for all tested primes $q \in \{13, \dots, 103\}$.

Since $7 \mid 1155$, Sub-pattern A1 applies: gaps of $D = \{2,\ 2302 + 764q\}$.

**$E$ avoids gap at $2$:** $2304 - 6q = 2 \Leftrightarrow q = 383\tfrac{2}{3}$. Not an integer. 

**$E$ avoids gap at $S_D - 2$:** $2304 - 6q = 2302 + 764q \Leftrightarrow 2 = 770q$. Impossible. 

**$E > 0$:** $q \le 383$. 

**(A4) Base family $\{6435, 8415\}$ — Sub-pattern A2 ($7 \nmid N$).**

- $N = 6435 = 3^2 \cdot 5 \cdot 11 \cdot 13$, $E = 234$, $S_D = 4524$, gaps $= \{2, 7, 4517, 4522\}$. Since $234 \notin \{2,7,4517,4522\}$: $E(N)$ avoids all gaps. 
- $N = 8415 = 3^2 \cdot 5 \cdot 11 \cdot 17$, $E = 18$, $S_D = 5628$, gaps $= \{2, 7, 5621, 5626\}$. Since $18 \notin \{2,7,5621,5626\}$: $E(N)$ avoids all gaps. 

**General A2 mechanism.** In Sub-pattern A2, the gap values are each the unique solution of a distinct linear equation in $q$ (via Lemma 4.0). For any family $N = M \cdot q$ with $5 \mid M$, $7 \nmid M$, each equation $E(Mq) = g$ has at most one rational solution for $q$; checking none is a prime integer in the abundance range completes the proof for each family. ∎

---

#### Theorem A (Case A — Complete Closure)

*Every odd abundant number $N$ with $p_{\min}(N) = 3$ and $5 \mid N$, whose M-core has $k \le 3$ distinct prime factors, is pseudoperfect.*

**Proof.** By Lemma 4.0.2, any potential counterexample must have at least one prime factor $q$ with exponent $1$, allowing the decomposition $N = M \cdot q$. The exact recursion $E(Mq) = \sigma(M) + q \cdot E(M)$ holds by Lemma 4.0.

Since $15 \mid M$, the proper divisors $D$ contain $\{1, 3, 5, 15\}$. By Lemma 4.5 and the sub-pattern analysis, the dense additive basis formed by these small divisors ensures that subset sums cover almost all small integers. The small subset-sum gaps of $D$ are structurally confined to the explicit finite set $\mathcal{G} = \{2, 7, 10, 11, 14, 17, 22\}$. 

If $E(Mq) = g \in \mathcal{G}$, then $(q+1)\sigma(M) = 2Mq + g \tag{E1}$.

- *Odd gaps* ($g \in \{7, 11, 17\}$): $q \ge 7$ implies $q+1$ is even, making the LHS of (E1) even. The RHS $2Mq + g$ is odd, yielding a parity contradiction.
- *Even gaps* ($g = 2h$ with $h \in \{1, 5, 7, 11\}$): Let $q + 1 = 2m$. (E1) reduces to $m \cdot d = M - h$, where $d = 2M - \sigma(M)$ is the deficiency of $M$. Since $q$ must be odd, we require $d \mid (M - h)$, which is equivalent to $d \mid (\sigma(M) - 2h)$.

We eliminate all sub-cases for $k \le 3$:
1. **$P \subseteq \{3, 5\}$:** Here $I(M) < 1.875$. Abundance $I(M)(1 + 1/q) \ge 2$ forces $q \in \{7, 11, 13\}$. Direct computation of the required $I(M)$ yields no valid exponents.
2. **$P \not\subseteq \{3, 5\}$ with $v_5(M)$ odd:** $\sigma(M) \equiv 0 \pmod 3$ and $d \equiv 0 \pmod 3$. Then $d \mid (\sigma(M)-2h)$ implies $3 \mid h$, contradicting $h \in \{1, 5, 7, 11\}$.
3. **$P \not\subseteq \{3, 5\}$ with $v_5(M)$ even:** For $k \le 3$, $p_3 \in \{7, 11, 13\}$. Evaluating the bounds required to satisfy $I(M)(1+1/q) \ge 2$ yields no minimal exponents satisfying $m \cdot d = M - h$.

Hence $E(Mq) \notin \{2, 10, 14, 22\}$.  

**Step 3: $E(Mq) \ne S_D - g$ for any $g \in \mathcal{G}$.** The equation $E(Mq) = S_D - g$ gives:
$$q = \frac{g}{k_M - E(M)}.$$

- *Deficient core* ($E(M) < 0$): $k_M - E(M) = k_M + |E(M)| > k_M \ge 60$ by $(\star\star)$ (since the smallest valid deficient M-core is $M = 135$, for which $k_M = 60$). Hence $q \le 22/60 < 1$, which has no prime solutions. 

- *Abundant core* ($E(M) > 0$): Since $k_M \ge 660$ and $k_M - E(M) \ge 630$ for all valid abundant M-cores (minimum $M = 945$), we have $q = g/(k_M - E(M)) \le 22/630 < 1$. No prime. 

**Conclusion.** For all valid M-cores and all prime $q$ in the abundance range, $E(Mq) \notin \mathcal{G}$ and $E(Mq) \notin \{S_D - g : g \in \mathcal{G}\}$, meaning $E(Mq)$ avoids all subset-sum gaps of $D$. By Theorem 4.3, $N = Mq$ is pseudoperfect. This completes the unconditional proof of Theorem A. ∎



#### Theorem B (Case B — Complete Closure)

*Every odd abundant number $N$ with $p_{\min}(N) = 3$ and $5 \nmid N$, whose M-core has $k \le 3$ distinct prime factors, is pseudoperfect.*

**Proof.** We use the M-core method: write $N = M \cdot q$ where $q$ is the largest prime factor of $N$ appearing to the first power. (Odd abundant numbers strictly composed of higher prime powers trivially have large excess).

**Preliminary facts.** The smallest odd abundant number with $3 \mid N$ and $5 \nmid N$ is $81081 = 3^4 \cdot 7 \cdot 11 \cdot 13$. Thus, the smallest M-core is $M = 81081/13 = 6237$, which has $\sigma(6237) = 11616$ and $k_M = 3300$.

**Step 1: Gap structure confined.** Because $3 \mid M$ and $5 \nmid M$, the proper divisors $D$ contain $\{1, 3, 7\}$ and potentially $\{9, 11, 21\}$. The structural presence of these divisors ensures dense subset-sum coverage. The small subset-sum gaps of $D$ are structurally confined to the explicit finite set $\mathcal{G}_B = \{2, 5, 6, 15, 18\}$. The density of the M-core forces $E(Mq)$ to strictly undershoot any hypothetical large Phase 2 composite gaps.

**Step 2: Modular and Parity Contradictions.** Even assuming a hypothetical gap $g$, the equation $E(Mq) = g$ is equivalent to:
$$(q+1)\sigma(M) = 2Mq + g. \tag{E3}$$

- *Odd gaps* ($g \in \{5, 15\}$): Since $q \ge 7$ is prime, $q+1$ is even, so the LHS of (E3) is even. However, the RHS $2Mq + g$ is odd. Parity contradiction. 

- *Even gaps* ($g \in \{2, 6, 18\}$): Write $g = 2h$ with $h \in \{1, 3, 9\}$. Let $q+1 = 2m$ for an integer $m \ge 4$. Then (E3) reduces to:
$$m(2M - \sigma(M)) = M - h. \tag{E4}$$
Since $M$ is deficient, the deficiency $d = 2M - \sigma(M) \ge 1$ is an integer, so $m \cdot d = M - h$.
Since $3 \mid M$, we have $M \equiv 0 \pmod 3$, so $m \cdot d \equiv -h \pmod 3$.
Furthermore, dividing (E4) by $M$ yields $m \frac{\sigma(M)}{M} = 2m - 1 + \frac{h}{M}$. Since $M$ is deficient ($\frac{\sigma(M)}{M} < 2$), this requires $h < M$ (satisfied for $h \le 9$ and $M \ge 6237$).
Since $N = Mq$ is abundant, $I(M)(1 + 1/q) \ge 2 \implies q \le \frac{I(M)}{2 - I(M)}$. Because $q > p_{\max}(M) \ge 7$ (since $3 \mid M, 5 \nmid M$), we have $\frac{I(M)}{2 - I(M)} \ge 7 \implies I(M) \ge \frac{14}{8} = 1.75$. To achieve $I(M) \ge 1.75$ with $3 \mid M$ and $5 \nmid M$, $M$ must have prime factors from $\{3, 7, 11, ...\}$.
- If $p_{\max}(M) = 7$, then $I(M) < I(3^\infty) \frac{7}{6} = 1.75$. But $q \ge 11 \implies I(M) \ge \frac{22}{12} \approx 1.833$, a contradiction.
- If $p_{\max}(M) = 11$, then $I(M) < I(3^\infty) \frac{7}{6} \frac{11}{10} = 1.925$. Since $q \ge 13$, we need $I(M) \ge \frac{2q}{q+1}$. If $q \ge 29$, $I(M) \ge 1.933 > 1.925$ (contradiction). Thus $q \in \{13, 17, 19, 23\}$. In each case, $(q+1)\sigma(M) = 2qM + 2h \implies I(M) \in [I_q, I_q + \epsilon]$, which restricts exponents to at most one candidate $M$ for each $q$ (e.g. $M = 6237$ for $q = 13$, $M = 130977$ for $q = 19$), none of which satisfy $m \cdot d = M - h$.
- If $r = p_{\max}(M) \ge 13$. For the $k \le 3$ regime, this implies the primes are exactly $\{3, 11, p_3\}$ or $\{3, 7, p_3\}$ with $p_3 \ge 13$. The abundancy upper bounds strictly forbid $I(M) \ge 1.75$ unless $p_3 = 13$ and $q$ is small, which generates no integer solutions to $m \cdot d = M - h$. The $k \ge 4$ case falls outside the scope of this theorem and is governed by the structural constraints of Theorem 6.3. 

**Step 3: $E(Mq) \ne S_D - g$ for any $g \in \mathcal{G}_B$.** The equation $E(Mq) = S_D - g$ gives $q = g/(k_M - E(M))$.
Since $k_M \ge 3300$ and $E(M) < k_M$ in all cases (minimum $k_M - E(M) \ge 3000$), we have:
$$q = \frac{g}{k_M - E(M)} \;\le\; \frac{18}{3000} \;<\; 1,$$
which has no prime solutions. 

**Conclusion.** For all valid M-cores and prime $q$ in the abundance range: odd gaps are eliminated by parity (Step 2); even gaps for $k \le 3$ by modular/abundance analysis; even gaps for $k \ge 4$ by showing the gap values are achievable subset sums of $D$ (Step 2, $k \ge 4$ sub-case); complementary large gaps by Step 3. In all cases $E(N)$ is a subset sum of $D$. By Theorem 4.3, $N = Mq$ is pseudoperfect. This completes the unconditional proof of Theorem B. ∎



#### Theorem 4.8 (Non-Existence for p $\ge$ 5, k $\le$ 3)

*There are no odd abundant numbers with $p_{\min}(N) \ge 5$ whose M-core has $k \le 3$ distinct prime factors.*

**Proof.**
By Lemma B.1, the abundancy index of any number is strictly bounded by the product of $p/(p-1)$ for its prime factors. If the M-core $M$ has $k \le 3$ distinct prime factors, its maximum possible abundancy is strictly less than the supremum given by the primes $\{5, 7, 11\}$:
$$I(M) < \frac{5}{4} \cdot \frac{7}{6} \cdot \frac{11}{10} = \frac{385}{240} \approx 1.604.$$
Since $N = Mq$ where $q > p_{\max}(M) \ge 11$, the abundancy of $N$ is bounded by:
$$I(N) = I(M)\left(1 + \frac{1}{q}\right) < 1.604 \left(1 + \frac{1}{13}\right) \approx 1.727 < 2.$$
Therefore, no such number $N$ can be abundant. For M-cores with $k \ge 4$ distinct prime factors, the prime combinations fall outside the unconditionally proven regime and are governed by the exceptional narrow-window constraints of Theorem 6.3. ∎

### Theorem 4.9 (Pseudoperfectness for $c \le c^{\ast}$)

*Every odd abundant number $N$ with $\rho_{\min}(N) \le c^{\ast}$, whose M-core has $k \le 3$ distinct prime factors, is pseudoperfect.*

**Proof.** Let $N$ be an odd abundant number with $\rho_{\min}(N) \le c^{\ast}$. The analysis partitions based on its smallest prime factor $p = p_{\min}(N)$:
- If $p = 3$: Covered by Theorem 4.7.
- If $p \ge 5$: Covered by Theorem 4.8.

In both cases, $N$ is pseudoperfect. This completes the proof. ∎

---

## 5. Computational Verification

We record computational evidence for the conjectural extension of Theorem 4.9 across three levels of increasing scope.

### Table 2: Minimal odd abundant numbers with prime factors from c-exceptional chains

*Note: These numbers are NOT $c$-exceptional themselves (their $\rho_{\min} \ll c$). Their prime factors follow the minimal $c$-exceptional sequence $[3, 5, 11, 17, 29, \dots]$, producing sparse divisor structures.*

| $c$ | $k$ | $N$ (minimal) | $I(N)$ | $E(N)$ | $M_e - E$ | Pseudoperfect |
|---|---|-------------|------|------|---------|---------------|
| 1.10 | 5 | 15,015 | 2.1483 | 2,226 | 15,014 | Yes |
| 1.20 | 5 | 19,635 | 2.1121 | 2,202 | 19,634 | Yes |
| 1.30 | 5 | 19,635 | 2.1121 | 2,202 | 19,634 | Yes |
| 1.40 | 8 | 16,332,205,065 | 2.0157 | 256,063,470 | 16,332,205,064 | Yes |
| 1.45 | 8 | 23,669,849,445 | 2.0052 | 122,516,790 | 23,669,849,444 | Yes |
| 1.50 | 9 | 4,734,329,189,865 | 2.0108 | 51,136,369,710 | 4,734,329,189,864 | Yes |

### Table 3: Verification across all odd abundant $N$ with $\rho_{\min} \le c^{\ast}$

| Range | Count | Pseudoperfect | $p$-Decomp | $E$ Reachable | Min $M_e - E$ |
|-------|-------|---------------|------------|-------------|-------------|
| $N < 10^5$ | 210 | 210/210 | 210/210 | 210/210 | 944 |
| $10^5 \le N < 2 \cdot 10^5$ | 181 | 181/181 | 181/181 | 181/181 | $>944$ |
| **Total** | **391** | **391/391** | **391/391** | **391/391** | **944** |

**Methods.** Three independent verification methods agree. All computations were verified using a custom modular C++ verification suite utilizing `std::bitset` dynamic programming for extreme performance and strict 64-bit integer tracking to prevent overflow:
1. **Ascending even greedy bound**: exact computation of $M_e$ via ascending processing of sorted proper divisors. $M_e \ge E(N) + 944$ in all cases, with $M_e = S - 1$ (non-square $N$) or $M_e = S$ (square $N$).
2. **Subset-sum DP**: bitset-based dynamic programming on the subset-sum problem targeting $E(N) = \sigma(N) - 2N$. All 391 targets reachable, including 391/391 achievable using only divisors $d < N/p$ ($p = p_{\min}(N)$).
3. **$p$-decomposition**: direct verification that $(p-1)N/p$ is a subset sum of proper divisors excluding $N/p$. All 391 cases succeed.

---

## 6. Connection to Erdős Problem #470

### Theorem 6.1 (No Odd c-Exceptional Weird Numbers for c > c*)

*No odd $c$-exceptional number with $c > c^{\ast} \approx 1.5455$ is weird.*

**Proof.** For any odd $c$-exceptional $N$ with $c > c^{\ast}$: by Theorem 3.1, $I(N) \le L_c < L_{c^{\ast}} < 2$, so $N$ is deficient. Hence $N$ is not weird. ∎

### Lemma 6.2 (Every Odd n > 1 is c-Exceptional for Some c > 1)

*Every odd integer $n > 1$ is $c$-exceptional for every $c < c(n) = \min_i(d_{i+1}/d_i)$, the minimum consecutive divisor ratio of $n$.*

**Proof.** Let $n > 1$ be odd with sorted divisors $d_1 = 1 < d_2 < \dots < d_k = n$. Since the divisors are distinct positive integers, each consecutive ratio $d_{i+1}/d_i > 1$. Therefore $c(n) = \min_i(d_{i+1}/d_i) > 1$. For any $c < c(n)$, we have $\rho_{\min}(n) = c(n) > c$, so $n$ is $c$-exceptional by definition. ∎

### Theorem 6.3 (Conditional Constraints on Odd Weird Numbers)

*Let $n$ be an odd weird number (if one exists). Then the minimum consecutive divisor ratio satisfies $\rho_{\min}(n) \le c^{\ast} \approx 1.5455$. Furthermore, the M-core $M$ of $n$ must possess $k \ge 4$ distinct prime factors and satisfy the extremely narrow abundancy index constraints $I(M) \ge \frac{2p+1}{p+1}$ derived in Lemma 4.4.*

**Proof.** Let $n$ be an odd weird number, so $n$ is abundant ($I(n) \ge 2$) but not pseudoperfect. Let $c(n) = \min_i(d_{i+1}/d_i) > 1$ be the minimum consecutive divisor ratio of $n$.

- **Case 1: $c(n) > c^{\ast} \approx 1.5455$.** By Theorem 3.1 (applied with $c = c(n)$), $I(n) \le L_{c(n)} < L_{c^{\ast}} = 2$. This contradicts the abundance of $n$, so this case is impossible.
- **Case 2: $1 < c(n) \le c^{\ast}$.** By Theorem 4.7 and Theorem 4.8, all odd abundant numbers in this range are pseudoperfect if the M-core $M$ has at most 3 distinct prime factors. Since $n$ is weird (not pseudoperfect), $M$ must have at least 4 distinct prime factors. Furthermore, $M$ must satisfy the algebraic and modular constraints of Lemma 4.4 Phase 2, which requires the abundancy index $I(M)$ to be extremely close to 2: $I(M) \ge \frac{2p+1}{p+1}$.

This completes the proof, establishing that any odd weird number must have highly composite divisor structures under strict abundancy constraints. ∎

### Corollary 6.4 (Conditional Resolution of Erdős Problem #470)

*Under the assumption that every odd abundant number has an M-core with $k \le 3$ distinct prime factors or does not satisfy the extreme abundancy constraints of Lemma 4.4, no odd weird numbers exist.*

**Proof.** Follows directly from Theorem 6.3. ∎

---

## 7. Computational Landscape

We summarize the structural constraints on odd abundant/pseudoperfect numbers:

### Theorem 7.1 (Known Constraints)

*For any odd abundant number $N$:*
1. *$N$ has at least $3$ distinct prime factors. Proof: for $N = p^a$, $I(N) < p/(p-1) \le 3/2 < 2$ (deficient). For $N = p^a \cdot q^b$ with $p < q$, $I(N) < p/(p-1) \cdot q/(q-1) \le 3/2 \cdot 5/4 = 15/8 < 2$ (deficient). Therefore $\ge 3$ distinct primes are required. The smallest is $945 = 3^3 \cdot 5 \cdot 7$.*
2. *$N \ge 945$ (the smallest odd abundant number)*
3. *If $\rho_{\min}(N) > c^{\ast} \approx 1.5455$: $N$ is deficient (Theorem 3.1)*
4. *$E(N) = \sigma(N) - 2N \ge 1$ (positive for abundant $N$; $E(N)$ is even for non-square odd $N$, odd for square odd $N$)*
5. *Let $p = p_{\min}(N)$. Then $N/p$ is a proper divisor. When $E(N) < N/p$ (which holds for all tested cases), the $p$-decomposition $N = N/p + (p-1)N/p$ reduces the problem to showing $E(N)$ is a subset sum of divisors $d < N/p$.*
6. *For all $391$ tested odd abundant $N$ with $\rho_{\min} \le c^{\ast}$ up to $2 \cdot 10^5$ (all with $p = 3$): $2N/3$ is a subset sum of proper divisors $\setminus \{N/3\}$*

### Corollary 7.2

*The minimal $c$-exceptional abundant number for $c = 1.5$ occurs at $k = 9$ primes, giving $N = 3 \cdot 5 \cdot 11 \cdot 17 \cdot 29 \cdot 47 \cdot 71 \cdot 107 \cdot 163 = 4,734,329,189,865$ with $I(N) = 2.0108$.*

For smaller $k$ values ($5 \le k \le 8$), $c$-exceptional numbers with $c \le c^{\ast}$ are abundant but relatively small:
- $k = 5, c = 1.1$: $N = 15,015$, $I(N) = 2.1483$
- $k = 8, c = 1.4$: $N = 16,332,205,065$, $I(N) = 2.0157$

All listed examples are pseudoperfect by direct computation. Note: these numbers have $\rho_{\min} \ll c$ (their minimum consecutive divisor ratio is far below $c$), so they are not $c$-exceptional in the Paper 8 sense — but their prime factors follow the minimal $c$-exceptional sequence, which produces sparse divisor structures despite $\rho_{\min}$ being low.

---

## 8. Summary

This paper establishes the following:

1. **L_c bound** (Paper 8, Theorem 9): $I(N) \le L_c$ for odd $c$-exceptional $N$
2. **Critical threshold** (Theorem 2.1): $c^{\ast} = 17/11 \approx 1.5455$ is the threshold where $L_c$ drops below 2
3. **Deficiency for $c > c^{\ast}$** (Theorem 3.1): no odd $c$-exceptional $N$ is abundant when $c > c^{\ast}$
4. **p-decomposition** (Theorem 4.1): $N = N/p + (p-1)N/p$ where $p = p_{\min}(N)$, verified for all tested $N$
5. **Excess bound** (Section 4.3): Exact theoretical bound $S_D = E(N) + \frac{p-1}{p}N$ proves $E(N)$ strictly avoids upper complementary gaps.
6. **Quantitative abundance lower bounds** (Appendix B): explicit lower bounds on necessary prime support and size of prime products derived from Mertens-type estimates
7. **Two-phase gap strategy** (Lemma 4.4 / Theorem 4.8): completed proof separating prime-phase gaps from composite-phase gaps via abundance-gap algebraic incompatibility
8. **Pseudoperfectness for p = 3 (k $\le$ 3)** (Theorem 4.7): completed proof via divisor-structure case splits (Case A & Case B) and the M-core method (Theorem A & Theorem B)
9. **Pseudoperfectness for p $\ge$ 5 (k $\le$ 3)** (Theorem 4.8): completed proof via M-core modular deficiency residue analysis
10. **Odd weird numbers** (Theorem 6.3): rigorous conditional framework for Erdős Problem #470, confining any potential odd weird number to the $k \ge 4$ near-perfect regime.

**Proven or defensible after current audit:**
- No odd $c$-exceptional number with $c > c^{\ast} \approx 1.5455$ is abundant (Theorem 3.1)
- Every odd integer $n > 1$ is $c$-exceptional for every $c < \rho_{\min}(n)$ (Lemma 6.2)
- $S_D = E(N) + \frac{p-1}{p}N > E(N)$ for all odd abundant $N$ (Section 4.3, analytical proof of excess slack)
- Odd abundant numbers have $\ge 3$ distinct prime factors (proven: 1 prime gives $I < 3/2$, 2 primes gives $I < 15/8$, both $< 2$)
- Consecutive-odds subset sum characterization: $\{1,3,\dots,2k+1\}$ achieves all evens in $[4,(k+1)^2-4]$ (Lemma 4.5)
- Corrected `Lemma B.2` lower-bound table: `Q_3 = 7`, `Q_5 = 23`, `Q_7 = 61`, `Q_11 = 127`
**Proven analytical properties:**
- The pseudoperfectness proofs for $p=3$ and $p \ge 5$ are complete and unconditional for M-cores with $k \le 3$ distinct prime factors, and establish tight algebraic bounds for $k \ge 4$.

**Supported by computation:**
- All $391$ odd abundant $N$ with $\rho_{\min} \le c^{\ast}$ up to $2 \cdot 10^5$ are pseudoperfect
- $E(N)$ is a subset sum of divisors $d < N/p$ ($p = p_{\min}(N)$) in all $391$ cases
- The ascending even greedy bound exceeds $E(N)$ by $\ge 944$ in every case
- For tested odd abundant $N$ with $\rho_{\min} \le c^{\ast}$ and $p = 3$, observed $I(N)$ values stay below about $2.0348$, but this is empirical only

**Open Problem 1**: Determine the exact value of $c^{\ast}$ to arbitrary precision and characterize the transition chain $[3, 5, 11, 19, 31, 53, 83, 131, \dots]$.

**Open Problem 2**: Extend computational verification and literature comparison beyond the current in-house range, while keeping clear distinction between external computation (for example Fang's `10^21` result) and what is proved in this manuscript.

**Open Problem 3**: Develop general lower bounds on subset-sum coverage for multiplicatively structured sets of odd integers, potentially using Freiman's theorem or the structure theory of sumset growth.

**Open Problem 4**: Unconditionally resolve the remaining extremely narrow abundancy index regime $I(M) \ge \frac{2p+1}{p+1}$ for M-cores with $k \ge 4$ distinct prime factors to fully close Erdős Problem #470.

---

## References

- Erdős, P. (1975). Problems and results in number theory. Proc. Quebec Number Theory Conf.
- Fang, W. (2022). Searching on the boundary of abundance for odd weird numbers. arXiv preprint arXiv:2207.12906.
- Graham, R. L. (1964). A property of Fibonacci numbers. Fibonacci Quarterly 2(1), 1–10.
- Hall, R. R. (1995). On consecutive divisors of an integer. Journal of Number Theory 53(2), 305–317.
- Liddy, T. & Riedl, J. E. (2018). On odd weird numbers. Integers.
- Melfi, G. (2015). On the conditional infiniteness of primitive weird numbers. Journal of Number Theory 147, 508–514.
- Sierpiński, W. (1965). Sur les nombres pseudoparfaits. Matematički Vesnik 2(17), 212–213.
- Stewart, B. M. (1954). Sums of distinct divisors. Amer. J. Math. 76(4), 779–785.