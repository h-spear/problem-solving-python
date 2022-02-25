# https://www.acmicpc.net/problem/21756

nums = [i for i in range(1, int(input()) + 1)]
nums.insert(0, 0)


def fn(nums):
    for i in range(1, len(nums), 2):
        if i & 1 == 1:
            nums[i] = -1

    while -1 in nums:
        del nums[nums.index(-1)]


while len(nums) > 2:
    fn(nums)

print(nums[1])
