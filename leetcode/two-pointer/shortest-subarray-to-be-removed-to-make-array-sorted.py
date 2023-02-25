# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
# ****
# https://www.youtube.com/watch?v=T3mVs4XHV1E


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        answer = 0
        n = len(arr)

        peak = 0
        while peak < n - 1 and arr[peak] <= arr[peak + 1]:
            peak += 1

        # already non-decreasing
        if peak == n - 1:
            return 0

        valley = n - 1
        while valley > peak and arr[valley - 1] <= arr[valley]:
            valley -= 1

        # first, second scenario
        answer = min(n - peak - 1, valley)

        # third scenario
        i = 0
        j = valley

        while i <= peak and j < n:
            if arr[j] >= arr[i]:
                answer = min(answer, j - i - 1)
                i += 1
            else:
                j += 1

        return answer
