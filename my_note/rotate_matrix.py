# pip install numpy
import numpy as np


def rotate_matrix_90(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def rotate_matrix_180(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[n - i - 1][m - j - 1] = A[i][j]
    return result


def rotate_matrix_270(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = A[i][j]
    return result


test = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2]]
array = np.array(test)
array_90 = np.array(rotate_matrix_90(test))
array_180 = np.array(rotate_matrix_180(test))
array_270 = np.array(rotate_matrix_270(test))

print(array)
print()

print(array_90)
print()

print(array_180)
print()

print(array_270)
print()
