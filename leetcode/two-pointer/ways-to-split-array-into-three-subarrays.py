# https://leetcode.com/problems/ways-to-split-array-into-three-subarraysways-to-split-array-into-three-subarrays/
# binary search: https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/discuss/1511845/Well-Coded-oror-Both-Method-oror-Two-Pointer-oror-Binary-Search


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        p = int(1e9) + 7
        n = len(nums)
        psum = [0]
        for num in nums:
            psum.append(psum[-1] + num)

        answer = 0
        left = 0
        right = 0
        for i in range(1, n):
            left = max(left, i + 1)
            while left < n and 2 * psum[i] > psum[left]:
                left += 1

            right = max(right, left)
            while right < n and 2 * psum[right] <= psum[i] + psum[-1]:
                right += 1

            answer += right - left

        return answer % p
