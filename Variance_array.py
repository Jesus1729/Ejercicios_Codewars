# Variance in a array of words

def variance(s):
    sop_X = [len(word) for word in s]
    e_X = 0
    for val in set(sop_X):
        e_X += val * sop_X.count(val)/len(sop_X)
    e_X2 = 0
    for val in set(sop_X):
        e_X2 += val**2 * sop_X.count(val)/len(sop_X)
    var = e_X2 - e_X**2
    return round(var,4)

print(variance(["Hi","world"]))