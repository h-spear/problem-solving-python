# https://www.acmicpc.net/problem/15663

from itertools import permutations

n, m = map(int, input().split())
nums = list(map(int, input().split()))
cases = set()
nums.sort()
for case in permutations(nums, m):
    cases.add(case)

cases = list(cases)
cases.sort()
for case in cases:
    for x in case:
        print(x, end=" ")
    print()
