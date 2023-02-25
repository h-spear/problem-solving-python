# https://leetcode.com/problems/build-array-from-permutation/


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            answer.append(nums[num])
        return answer
