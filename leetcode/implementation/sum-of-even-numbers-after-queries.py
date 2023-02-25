# https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        output = []
        curr = 0
        for num in nums:
            if num & 1 == 0:
                curr += num

        for val, idx in queries:
            if nums[idx] & 1 == 0:
                curr -= nums[idx]

            nums[idx] += val

            if nums[idx] & 1 == 0:
                curr += nums[idx]

            output.append(curr)

        return output
