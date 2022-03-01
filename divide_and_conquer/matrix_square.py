# https://www.acmicpc.net/problem/10830
# 참고: https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5


def mul(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            result[i][j] = temp % 1000

    return result


def power(A, b):
    n = len(A)
    if b == 1:
        for i in range(n):
            for j in range(n):
                A[i][j] %= 1000
        return A

    temp = power(A, b // 2)
    if b & 1:
        return mul(mul(temp, temp), A)
    else:
        return mul(temp, temp)


n, b = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

result = power(a, b)
for r in result:
    print(*r)
