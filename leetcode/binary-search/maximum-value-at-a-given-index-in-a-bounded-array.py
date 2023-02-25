# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def add(l, x):
            if l >= x:
                return int((x * (x - 1) / 2) + (l - x + 1))
            else:
                return int((l / 2) * (2 * (x - 1) - (l - 1)))

        def f(x):
            if x == 1:
                return n

            left = index
            right = n - index - 1
            return x + add(left, x) + add(right, x)

        left = 1
        right = maxSum
        answer = 0
        while left <= right:
            mid = (left + right) // 2

            if f(mid) > maxSum:
                right = mid - 1
            else:
                left = mid + 1
                answer = mid

        return answer
