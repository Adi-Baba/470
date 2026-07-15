from sympy import primerange

def I(a, b, c, d):
    s3 = (3**(a+1)-1)//2 if a>0 else 1
    s5 = (5**(b+1)-1)//4 if b>0 else 1
    s7 = (7**(c+1)-1)//6 if c>0 else 1
    s11 = (11**(d+1)-1)//10 if d>0 else 1
    m = (3**a) * (5**b) * (7**c) * (11**d)
    if m == 1: return 0, 1, 1
    return (s3*s5*s7*s11) / m, m, s3*s5*s7*s11

found = False
for q in primerange(13, 100):
    target = 2 * q / (q + 1)
    for a in range(1, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    val, m_prime, sig_m_prime = I(a, b, c, d)
                    for pk in primerange(13, q):
                        # M = M' * pk
                        # I(M) = I(M') * (pk+1)/pk  -- assuming pk is prime to M'
                        if pk in [3, 5, 7, 11]: continue
                        I_M = val * (pk + 1) / pk
                        if target < I_M < 2:
                            if pk > sig_m_prime:
                                print(f"COUNTEREXAMPLE FOUND!")
                                print(f"q={q}, pk={pk}, M'={m_prime}, sig(M')={sig_m_prime}, I(M)={I_M}")
                                found = True
if not found:
    print("No counterexample found.")
