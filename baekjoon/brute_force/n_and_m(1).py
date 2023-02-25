# https://www.acmicpc.net/problem/15649

from itertools import permutations

n, m = map(int, input().split())
for case in permutations(range(1, n + 1), m):
    print(" ".join(map(str, case)))
