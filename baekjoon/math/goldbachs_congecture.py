# https://www.acmicpc.net/problem/9020

A = [True] * 10001
A[0], A[1] = False, False
for i in range(2, int(10001 ** 0.5) + 1):
    if A[i]:
        j = 2
        while i * j <= 10000:
            A[i * j] = False
            j += 1


def goldbachs_congecture(n):
    s = n // 2
    for i in range(s, n):
        if A[i] and A[n - i]:
            return n - i, i


for tc in range(int(input())):
    n = int(input())
    print(*goldbachs_congecture(n))
