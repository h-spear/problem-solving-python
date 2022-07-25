# https://www.acmicpc.net/problem/15664

from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))

candidates = set()

for candidate in combinations(a, m):
    candidate = list(candidate)
    candidate.sort()
    candidate = tuple(candidate)
    candidates.add(candidate)

candidates = list(candidates)
candidates.sort()

for candidate in candidates:
    print(*candidate)
