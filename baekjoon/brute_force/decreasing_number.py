# https://www.acmicpc.net/problem/1038

from itertools import combinations

nums = [i for i in range(10)]
dec_nums = []

for i in range(1, 11):
    for x in combinations(nums, i):
        dec_nums.append(int("".join(list(map(str, sorted(x, reverse=True))))))

n = int(input())
dec_nums.sort()

if n >= len(dec_nums):
    print(-1)
else:
    print(dec_nums[n])
