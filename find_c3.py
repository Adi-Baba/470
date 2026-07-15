from sympy import nextprime
def check_c(num, den):
    q = 3
    prod = 1.5
    for _ in range(20):
        q = nextprime(int(num * q / den))
        prod *= (q / (q - 1))
    return prod

print("13/7:", check_c(13, 7))
print("12/7:", check_c(12, 7))
print("11/6:", check_c(11, 6))

