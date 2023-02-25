# https://leetcode.com/problems/minimum-size-subarray-sum/
# binary search + prefix sum
# O(nlog(n))
# two pointer : O(n)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        def find(left, right, key):
            while left < right:
                mid = int(left + (right - left) / 2)
                if psum[mid] >= key:
                    right = mid
                else:
                    left = mid + 1

            return left

        INF = 123456789
        n = len(nums)
        psum = [nums[0]]
        answer = INF
        for i in range(1, n):
            psum.append(psum[-1] + nums[i])

        for i in range(n):
            right = find(i, n, target + psum[i] - nums[i])
            if right < n:
                answer = min(answer, right - i + 1)

        if answer == INF:
            return 0
        return answer
