# https://www.acmicpc.net/problem/13977

import sys

input = lambda: sys.stdin.readline().rstrip()


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

factorial = [0] * 4000001
factorial[0] = 1
factorial[1] = 1
for i in range(2, 4000001):
    factorial[i] = (factorial[i - 1] * i) % p

for tc in range(int(input())):
    n, k = map(int, input().split())
    a = factorial[n]
    b = (factorial[n - k] * factorial[k]) % p
    print((a * pow(b, p - 2)) % p)
