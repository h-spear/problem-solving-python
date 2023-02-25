# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        ld = len(dist)

        def f(x):
            f_res = 0

            for i, d in enumerate(dist):
                if i == ld - 1:
                    f_res += d / x
                else:
                    f_res += math.ceil(d / x)

            return f_res

        left = 1
        right = int(1e7)
        answer = -1
        while left <= right:
            mid = (left + right) // 2

            if f(mid) > hour:
                left = mid + 1
            else:
                right = mid - 1
                answer = mid

        return answer
