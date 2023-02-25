# https://www.acmicpc.net/problem/11444
# https://www.acmicpc.net/blog/view/28


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


def power(A, n):
    if n == 1:
        return A

    temp = power(A, n // 2)
    if n & 1:
        return mul(mul(temp, temp), A)
    else:
        return mul(temp, temp)


n = int(input())
m = [[1, 1], [1, 0]]
print(power(m, n)[0][1])
