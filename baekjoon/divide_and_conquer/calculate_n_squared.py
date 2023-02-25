# https://www.acmicpc.net/problem/12728
# https://www.acmicpc.net/problem/12925
# https://seokjin2.tistory.com/13


def matrix_multiplication(A, B):
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            temp = 0
            for k in range(2):
                temp += A[i][k] * B[k][j]
            C[i][j] = temp % p
    return C


def matrix_power(A, n):
    if n == 1:
        return A

    temp = matrix_power(A, n // 2)
    if n & 1:
        return matrix_multiplication(matrix_multiplication(temp, temp), A)
    else:
        return matrix_multiplication(temp, temp)


p = 1000
for tc in range(1, int(input()) + 1):
    n = int(input())
    A = [[6, -4], [1, 0]]
    R = matrix_power(A, n - 1)
    cn = (28 * R[1][0] + 6 * R[1][1] - 1) % p
    print("Case #{}: {}".format(tc, str(cn).zfill(3)))
