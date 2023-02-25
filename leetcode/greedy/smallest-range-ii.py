# https://leetcode.com/problems/smallest-range-ii/


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = nums[0]
        high = nums[-1]
        answer = high - low

        for i in range(len(nums) - 1):
            high = max(high, nums[i] + 2 * k)
            low = min(nums[0] + 2 * k, nums[i + 1])
            answer = min(answer, high - low)

        return answer


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = nums[-1] - nums[0]

        for i in range(1, len(nums)):
            left = nums[:i]
            right = nums[i:]

            minn = min(left[0] + k, right[0] - k)
            maxx = max(left[-1] + k, right[-1] - k)
            answer = min(answer, maxx - minn)

        return answer
