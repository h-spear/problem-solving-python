# https://leetcode.com/problems/third-maximum-number/


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = list(set(nums))
        distinct.sort(reverse=True)

        if len(distinct) < 3:
            return max(distinct)
        else:
            return distinct[2]
