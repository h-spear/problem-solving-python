# https://www.acmicpc.net/problem/15652

from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = [(i + 1) for i in range(n)]
for case in combinations_with_replacement(nums, m):
    print(" ".join(map(str, case)))
