# https://www.acmicpc.net/problem/11778

import math


def matrix_multiplication(A, B):
    la = len(A)
    lac = len(A[0])
    lbc = len(B[0])
    C = [[0] * lbc for _ in range(la)]
    for i in range(la):
        for j in range(lbc):
            temp = 0
            for k in range(lac):
                temp += A[i][k] * B[k][j]
            C[i][j] = temp % p
    return C


def matrix_power(A, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return A

    temp = matrix_power(A, n // 2)
    if n & 1:
        return matrix_multiplication(matrix_multiplication(temp, temp), A)
    else:
        return matrix_multiplication(temp, temp)


p = 1000000007
n, m = map(int, input().split())
_gcd = math.gcd(n, m)
A = [[1, 1], [1, 0]]
r = matrix_power(A, _gcd)
print(r[0][1] % p)
