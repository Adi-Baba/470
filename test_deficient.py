from sympy import primefactors

def I(m):
    sig = 1
    for p in primefactors(m):
        temp = m
        c = 0
        while temp % p == 0:
            c += 1
            temp //= p
        sig *= (p**(c+1) - 1) // (p - 1)
    return sig / m

best_m = 0
best_I = 0
for m in range(3, 100000, 2):
    val = I(m)
    if val < 2 and val > best_I:
        best_I = val
        best_m = m
        print(f"New best deficient: {m} with I = {val:.5f}")
