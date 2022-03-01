# 행렬의 곱
def mul(A, B):
    la = len(A)
    lac = len(A[0])
    lbc = len(B[0])
    result = [[0] * lbc for _ in range(la)]
    for i in range(la):
        for j in range(lbc):
            temp = 0
            for k in range(lac):
                temp += A[i][k] * B[k][j]
            result[i][j] = temp % 1000000007
    return result


def mulmod(A, B, p):
    la = len(A)
    lac = len(A[0])
    lbc = len(B[0])
    result = [[0] * lbc for _ in range(la)]
    for i in range(la):
        for j in range(lbc):
            temp = 0
            for k in range(lac):
                temp += A[i][k] * B[k][j]
            result[i][j] = temp % p
    return result


# 행렬의 제곱
def power(A, n):
    if n == 1:
        return A

    temp = power(A, n // 2)
    if n & 1:
        return mul(mul(temp, temp), A)
    else:
        return mul(temp, temp)
