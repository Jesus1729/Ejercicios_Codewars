# Sierpinski's Gasket

def sierpinski(n):
    if n == 0:
        return 'L'
    prev = sierpinski(n-1).split('\n')
    #n = len(prev[-1])
    return '\n'.join(prev + [s.ljust(2**n) + s for s in prev])

print(sierpinski(4))