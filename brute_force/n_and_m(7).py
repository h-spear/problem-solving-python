# https://www.acmicpc.net/problem/15656

from itertools import product

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
cases = []
for case in product(nums, repeat=m):
    print(" ".join(map(str, case)))
