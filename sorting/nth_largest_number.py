# https://www.acmicpc.net/problem/2075

n = int(input())
nums = []
for _ in range(n):
    nums.extend(list(map(int, input().split())))
    nums.sort(reverse=True)
    nums = nums[:n]

print(nums[-1])
