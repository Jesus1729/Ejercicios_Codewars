# Transpose of a Matrix

def transpose(arr):
    t = []
    for j in range(len(arr[0])):
        t.append([])
        for i in range(len(arr)):
            t[-1].append(arr[i][j])
    return t

print(transpose([[1,2,3],[4,5,6]]))