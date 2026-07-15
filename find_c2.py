from sympy import nextprime
for c_val in range(1750, 1900):
    c = c_val / 1000.0
    q = 3
    prod = 1.5
    chain = [3]
    for _ in range(10):
        q = nextprime(int(c * q))
        chain.append(q)
        prod *= (q / (q - 1))
    if prod < 2.0:
        print(f"c={c} gives prod={prod} chain={chain}")
        break

