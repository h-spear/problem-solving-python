# https://www.acmicpc.net/problem/11401
# 페르마의 소정리 : 1/a = a^(p-2) [mod p]
n, k = map(int, input().split())
p = 1000000007


def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return res


def pow(n, s):
    if s == 0:
        return 1
    elif s == 1:
        return n

    tmp = pow(n, s // 2)
    if s & 1:
        return (tmp * tmp * n) % p
    else:
        return (tmp * tmp) % p


a = factorial(n)
b = factorial(n - k) * factorial(k)
print((a * pow(b, p - 2)) % p)
