# Maximum Multiple

def max_multiple(divisor, bound):
    aux = []
    for i in range(1,bound+1):
        if i%divisor==0:
            aux.append(i)
    return max(aux)

print(max_multiple(2,15))