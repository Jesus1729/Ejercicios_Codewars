# Square Matrix Multiplication

def matrix_mult(a, b):
    C = []
    for i in range(len(a)):
        C.append([])
        for j in range(len(a)):
            sum = 0
            for k in range(len(a)):
                sum+= a[i][k]*b[k][j]
            C[-1].append(sum)
    return C

print(matrix_mult(
  [ [9, 7],
    [0, 1] ],
  [ [1, 1],
    [4, 12] ]))