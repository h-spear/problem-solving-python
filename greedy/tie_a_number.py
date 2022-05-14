# https://www.acmicpc.net/problem/1744

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

answer = 0
zero_cnt = 0
while len(nums) >= 2 and nums[-1] > 1 and nums[-2] > 1:
    one = nums.pop()
    two = nums.pop()
    answer += one * two

while nums and nums[-1] == 1:
    nums.pop()
    answer += 1

nums.sort(reverse=True)
while len(nums) >= 2 and nums[-1] < 0 and nums[-2] < 0:
    one = nums.pop()
    two = nums.pop()
    answer += one * two

zero_cnt = nums.count(0)
for i in range(len(nums) - 1, len(nums) - zero_cnt - 1, -1):
    if nums[i] < 0:
        nums[i] = 0
answer += sum(nums)

print(answer)
