# Arithmetic sequence - sum of n elements

def arithmetic_sequence_sum(a, r, n):
    a_1 = a
    a_n = a_1 + (n-1)*r
    return n*(a_1+a_n)/2

print(arithmetic_sequence_sum(1,2,5))