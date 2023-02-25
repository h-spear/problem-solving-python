# https://www.acmicpc.net/problem/10844

n = int(input())
nums = [0] * 11
for i in range(1, 10):
    nums[i] = 1

for i in range(1, n):
    temp = [0] * 11
    for j in range(0, 10):
        temp[j] = nums[j - 1] + nums[j + 1]
    nums = temp

print(sum(nums) % 1000000000)
