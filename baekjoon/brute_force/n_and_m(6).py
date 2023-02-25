# https://www.acmicpc.net/problem/15655

from itertools import combinations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cases = []
for case in combinations(nums, m):
    print(" ".join(map(str, case)))
