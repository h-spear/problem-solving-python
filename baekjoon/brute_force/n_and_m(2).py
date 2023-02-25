# https://www.acmicpc.net/problem/15650

from itertools import combinations

n, m = map(int, input().split())
nums = [(i + 1) for i in range(n)]
for case in combinations(nums, m):
    print(" ".join(map(str, case)))
