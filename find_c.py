def find_c():
    from sympy import nextprime
    
    # We want to find a c where L_c = prod q_k / (q_k - 1) < 2
    # Let's test a range of c values from 1.5 to 3.0
    for c_val in range(150, 300):
        c = c_val / 100.0
        q = 3
        prod = 1.5
        for _ in range(10):
            q = nextprime(int(c * q))
            prod *= (q / (q - 1))
        if prod < 2.0:
            print(f"c={c} gives prod={prod}")
            break

find_c()
