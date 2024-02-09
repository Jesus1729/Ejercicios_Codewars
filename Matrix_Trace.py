# Matrix Trace

def trace(m):
    if len(m)==0:
        return None
    elif len(m) != len(m[0]):
        return None
    else:
        return sum([m[j][i] for i in range(len(m)) for j in range(len(m)) if i==j])

trace([[1,2],[3,4]])