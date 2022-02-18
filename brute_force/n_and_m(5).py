# https://www.acmicpc.net/problem/15654

from itertools import permutations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
for case in permutations(nums, m):
    print(" ".join(map(str, case)))
