# https://www.acmicpc.net/problem/18291


def powmod(C, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * C
        C = C * C % mod
        n >>= 1
    return res % mod


MAX = 10 ** 9 + 7
for tc in range(int(input())):
    cnt = int(input())
    if cnt == 1:
        print(1)
    elif cnt == 2:
        print(1)
    else:
        print(powmod(2, cnt - 2, MAX))
