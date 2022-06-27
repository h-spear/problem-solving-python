# https://www.acmicpc.net/problem/5095


def matrix_multiplication(A, B, n, m):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            C[i][j] = temp % m
    return C


def matrix_power(A, b, n, m):
    if b == 1:
        return A

    temp = matrix_power(A, b // 2, n, m)
    if b & 1:
        return matrix_multiplication(matrix_multiplication(temp, temp, n, m), A, n, m)
    else:
        return matrix_multiplication(temp, temp, n, m)


def print_matrix(A, n):
    for i in range(n):
        for j in range(n):
            print(A[i][j], end="")
            if j < n - 1:
                print(" ", end="")
        print()
    print()


while 1:
    n, m, p = map(int, input().split())
    if n == 0 and m == 0 and p == 0:
        break
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            A[i][j] %= m

    print_matrix(matrix_power(A, p, n, m), n)
