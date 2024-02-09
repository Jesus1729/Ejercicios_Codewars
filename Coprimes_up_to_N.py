# Coprimes up to N

import math

def coprimes(n):
    return [i for i in range(1,n) if math.gcd(n,i) == 1]

print(coprimes(10))