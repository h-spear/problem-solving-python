# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        def find(arr, num):
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] >= num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left - 1

        answer = 0
        for i, num in enumerate(nums1):
            f_idx = find(nums2, num)
            answer = max(f_idx - i, answer)

        return answer
