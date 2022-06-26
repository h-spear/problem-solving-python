# https://www.acmicpc.net/problem/2749
# https://www.acmicpc.net/blog/view/28


def matrix_multiplication(A, B):
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            temp = 0
            for k in range(2):
                temp += (A[i][k] * B[k][j]) % p
            C[i][j] = temp
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


p = 1000000
n = int(input())
A = [[1, 1], [1, 0]]
P = matrix_power(A, n)

print(P[0][1] % p)
