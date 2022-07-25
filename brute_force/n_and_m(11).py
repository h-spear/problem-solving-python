# https://www.acmicpc.net/problem/15665

from itertools import product

n, m = map(int, input().split())
a = list(map(int, input().split()))

candidates = set()
for candidate in product(a, repeat=m):
    candidate = tuple(candidate)
    candidates.add(candidate)

candidates = list(candidates)
candidates.sort()

for candidate in candidates:
    print(*candidate)
