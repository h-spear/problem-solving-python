# https://leetcode.com/problems/arithmetic-subarrays/


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        def is_arithmetic(arr):
            n = len(arr)
            arr.sort()
            diff = arr[1] - arr[0]
            for i in range(1, n):
                if arr[i] - arr[i - 1] != diff:
                    return False
            return True

        output = []
        for ll, rr in zip(l, r):
            arr = nums[ll : rr + 1].copy()
            output.append(is_arithmetic(arr))

        return output
