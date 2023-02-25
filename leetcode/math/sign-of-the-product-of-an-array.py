# https://leetcode.com/problems/sign-of-the-product-of-an-array/


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                negative_count += 1

        if negative_count & 1:
            return -1
        else:
            return 1
