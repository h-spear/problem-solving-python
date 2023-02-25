# https://leetcode.com/problems/partition-equal-subset-sum/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        half = total // 2
        dp = set()
        dp.add(0)

        for num in nums:
            temp = set()
            for past in dp:
                temp.add(past + num)
            dp.update(temp)

            if half in dp:
                return True

        return False
