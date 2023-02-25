# https://leetcode.com/problems/find-a-peak-element-ii/
# ***


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        peaks = []
        for x in mat:
            peaks.append(max(x))

        left = 0
        right = m - 1
        idx = m - 1
        while left <= right:
            mid = left + (right - left) // 2
            if peaks[mid] > peaks[right]:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        return [idx, mat[idx].index(peaks[idx])]
