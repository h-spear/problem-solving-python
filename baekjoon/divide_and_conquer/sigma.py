# https://www.acmicpc.net/problem/13172

import math


def powmod(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


m = int(input())
p = 1000000007
sum = 0
for _ in range(m):
    n, s = map(int, input().split())

    # 기약분수로 만듬
    gcd = math.gcd(n, s)
    n //= gcd
    s //= gcd

    sum += s * powmod(n, p - 2, p)
    sum %= p

print(sum)
