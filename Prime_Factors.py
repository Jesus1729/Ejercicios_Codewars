# Prime Factors

from gmpy2 import is_prime

def prime_factors(n):
    fact_primos = []
    if n == 1:
        return []
    elif is_prime(n):
        return [n]
    else:
        i = 2
        while n!=1:
            if is_prime(i) == True and n%i == 0:
                fact_primos.append(i)
                n = n/i
            else:
                i += 1
        return fact_primos

print(prime_factors(20))