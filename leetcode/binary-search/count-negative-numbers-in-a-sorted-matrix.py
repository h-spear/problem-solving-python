# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def get_negative_count_by_one_dimen(arr):
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1

            return n - left

        m = len(grid)
        n = len(grid[0])
        negative_count = 0

        for i in range(m):
            negative_count += get_negative_count_by_one_dimen(grid[i])

        return negative_count
