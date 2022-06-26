# https://www.acmicpc.net/problem/2086


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


p = 1000000000
a, b = map(int, input().split())
A = [[1, 1], [1, 0]]
sum_to_b = matrix_power(A, b + 2)[0][1] - 1
sum_to_a_minus_1 = matrix_power(A, a + 1)[0][1] - 1
print((sum_to_b - sum_to_a_minus_1) % p)
