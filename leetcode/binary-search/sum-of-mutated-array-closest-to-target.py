# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def convert(x):
            total = 0
            for num in arr:
                if num >= x:
                    total += x
                else:
                    total += num
            return total

        left = 0
        right = max(arr)
        ub = 0

        while left <= right:
            mid = (left + right) // 2

            val = convert(mid)
            if val >= target:
                ub = mid
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = max(arr)
        lb = 0
        while left <= right:
            mid = (left + right) // 2

            val = convert(mid)
            if val <= target:
                lb = mid
                left = mid + 1
            else:
                right = mid - 1

        print(lb, ub)
        if abs(target - convert(lb)) <= abs(target - convert(ub)):
            return lb
        else:
            return ub
