# Estimating Amounts of Subsets

def est_subsets(arr):
    return 2**len(set(arr)) - 1

est_subsets({1, 2, 3, 4})