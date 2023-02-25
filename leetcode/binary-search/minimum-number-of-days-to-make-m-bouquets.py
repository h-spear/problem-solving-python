# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        def f(x):
            seq = 0
            res = 0
            for day in bloomDay:
                if day <= x:
                    seq += 1
                else:
                    seq = 0

                if seq == k:
                    seq = 0
                    res += 1

            return res

        left = 1
        right = max(bloomDay)
        answer = -1
        while left <= right:
            mid = (left + right) // 2

            if f(mid) < m:
                left = mid + 1
            else:
                right = mid - 1
                answer = mid

        return answer
