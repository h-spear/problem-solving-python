# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        p = int(1e9) + 7
        subsums = []

        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                subsums.append(curr)

        subsums.sort()
        return sum(subsums[left - 1 : right]) % p
