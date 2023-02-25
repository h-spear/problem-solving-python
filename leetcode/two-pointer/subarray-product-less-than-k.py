# https://leetcode.com/problems/subarray-product-less-than-k/


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        curr = 1
        answer = 0

        for j in range(n):
            curr *= nums[j]
            while curr >= k and i < n:
                curr //= nums[i]
                i += 1

            if i <= j:
                answer += j - i + 1

        return answer
