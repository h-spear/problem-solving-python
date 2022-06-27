# https://www.acmicpc.net/problem/16134


def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res = (res * i) % p
    return res


def pow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a

    temp = pow(a, n // 2)
    if n & 1:
        return (temp * temp * a) % p
    else:
        return (temp * temp) % p


p = 1000000007
n, r = map(int, input().split())
a = factorial(n)
b = (factorial(n - r) * factorial(r)) % p
print((a * pow(b, p - 2)) % p)
