from sympy import nextprime
q = 3
prod = 1.5
for _ in range(20):
    val = 13.0/7.0 * q - 0.0001
    q = nextprime(int(val))
    prod *= (q / (q - 1))
print("13/7 - eps:", prod)
