from sympy import primerange, primefactors

def I(m):
    sig = 1
    for p in primefactors(m):
        temp = m
        c = 0
        while temp % p == 0:
            c += 1
            temp //= p
        sig *= (p**(c+1) - 1) // (p - 1)
    return sig / m, sig

def check():
    for q in primerange(13, 2000):
        target = 2 * q / (q + 1)
        for pk in primerange(13, q):
            # We want M' < pk  (which implies sig(M') < 2*pk, likely < pk if deficient)
            # Actually we want sig(M') < pk
            for m_prime in range(3, pk, 2):
                if pk in primefactors(m_prime): continue
                val, sig_m_prime = I(m_prime)
                if sig_m_prime >= pk: continue
                
                I_M = val * (pk + 1) / pk
                if target < I_M < 2:
                    print(f"COUNTEREXAMPLE FOUND: q={q}, pk={pk}, M'={m_prime}, sig(M')={sig_m_prime}, I(M)={I_M}")
                    return True
    print("No counterexample found in wide search.")
    return False

check()
