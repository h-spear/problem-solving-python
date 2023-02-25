# https://www.acmicpc.net/problem/13246


def identify_matrix(n):
    I = [[0] * n for _ in range(n)]
    for i in range(n):
        I[i][i] = 1
    return I


def matrix_multiplication(A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            C[i][j] = temp % p
    return C


def matrix_power(A, b):
    if b == 0:
        return identify_matrix(n)
    elif b == 1:
        return A

    temp = matrix_power(A, b // 2)
    if b & 1:
        return matrix_multiplication(matrix_multiplication(temp, temp), A)
    else:
        return matrix_multiplication(temp, temp)


def matrix_addition(A, B):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = (A[i][j] + B[i][j]) % p
    return C


def matrix_power_summation(A, b):
    if b == 0:
        return [[0] * n for _ in range(n)]
    elif b == 1:
        return A

    if b & 1:
        return matrix_addition(
            matrix_power_summation(A, b - 1),
            matrix_power(A, b),
        )
    else:
        return matrix_multiplication(
            matrix_addition(matrix_power(A, b // 2), identify_matrix(n)),
            matrix_power_summation(A, b // 2),
        )


p = 1000
n, b = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if A[i][j] == 1000:
            A[i][j] = 0

S = matrix_power_summation(A, b)
for i in range(n):
    for j in range(n):
        print(S[i][j], end=" ")
    print()
