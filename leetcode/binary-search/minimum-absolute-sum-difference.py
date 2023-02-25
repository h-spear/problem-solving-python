# https://leetcode.com/problems/minimum-absolute-sum-difference/

from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        def get_minima(arr, x):
            idx = bisect_left(arr, x)
            if idx != 0 and idx != n:
                return min(abs(x - arr[idx]), abs(x - arr[idx - 1]))
            elif idx == 0:
                return abs(x - arr[idx])
            else:
                return abs(x - arr[idx - 1])

        n = len(nums1)
        answer = float("inf")
        p = 1000000007
        extras = []
        for num1, num2 in zip(nums1, nums2):
            extras.append(abs(num1 - num2))

        total = sum(extras)
        nums1.sort()
        for i, num2 in enumerate(nums2):
            answer = min(answer, total - extras[i] + get_minima(nums1, num2))

        return answer % p
