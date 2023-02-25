# https://www.acmicpc.net/problem/15657

from itertools import combinations_with_replacement

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cases = []
for case in combinations_with_replacement(nums, m):
    print(" ".join(map(str, case)))
