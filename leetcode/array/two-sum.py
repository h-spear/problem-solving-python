# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, num in enumerate(nums):
            t = target - num

            if t in nums[idx + 1 :]:
                return [idx, nums[idx + 1 :].index(t) + idx + 1]

        return None
