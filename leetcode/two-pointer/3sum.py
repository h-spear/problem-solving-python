# https://leetcode.com/problems/3sum/

# 9373ms
from bisect import bisect_left


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        temp = [(num, idx) for idx, num in enumerate(nums)]
        temp.sort()
        nums = []
        idxs = []

        for num, idx in temp:
            nums.append(num)
            idxs.append(idx)

        answer = set()
        for i in range(n):
            for j in range(i + 1, n):
                key = 0 - (nums[i] + nums[j])
                lb = bisect_left(nums, key, lo=j + 1)
                if lb < n and nums[lb] == key:
                    answer.add((nums[i], nums[j], nums[lb]))

        return list(answer)


# 1197ms
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)):
            # 시간 단축 1 : 같은 원소인 경우 점프
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            now = nums[i]
            target = -now

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    answer.append([now, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
        return answer
