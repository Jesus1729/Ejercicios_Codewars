# Matrix Determinant

import numpy
def determinant(matrix):
    return round(numpy.linalg.det(matrix))

print(determinant([[4, 6], [3,8]]))