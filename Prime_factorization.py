# Prime factorization

from gmpy2 import is_prime

class PrimeFactorizer:
    # Constructor
    def __init__(self,n:int):
        self.n = n
        self.factor = {}

        factores_primos = []

        if self.n == 1:
            return self.n
        else:
            i = 2
            while self.n != 1:
                if is_prime(i) == True and self.n%i == 0:
                    factores_primos.append(i)
                    self.n = self.n/i
                else:
                    i+=1

        self.factor = {factores_primos[i]:factores_primos.count(factores_primos[i]) for i in range(len(factores_primos))}

print(PrimeFactorizer(24).factor)