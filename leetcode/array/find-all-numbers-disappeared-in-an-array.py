# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# ****


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])

        for i, num in enumerate(nums):
            if num > 0:
                answer.append(i + 1)

        return answer
