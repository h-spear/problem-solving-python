# https://www.acmicpc.net/problem/15651

from itertools import product

n, m = map(int, input().split())
for case in product(range(1, n + 1), repeat=m):
    print(" ".join(map(str, case)))
