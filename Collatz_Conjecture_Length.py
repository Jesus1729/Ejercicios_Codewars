# Collatz Conjecture Length

def collatz(n):
    l = []
    while n >= 1:
        if n%2 == 0:
            n = n//2
            l.append(n)
            if n==1:
                break
        else:
            n = 3*n + 1
            l.append(n)
            if n==1:
                break
    return len(l) + 1

collatz(20)