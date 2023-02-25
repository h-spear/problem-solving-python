# https://www.acmicpc.net/problem/1235

n = int(input())
nums = []
for _ in range(n):
    nums.append(input())

ln = len(nums[0])
for i in range(ln - 1, -1, -1):
    temp = set()
    for num in nums:
        temp.add(num[i:])

    if len(temp) == n:
        print(ln - i)
        exit(0)
