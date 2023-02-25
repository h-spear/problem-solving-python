# https://leetcode.com/problems/magnetic-force-between-two-balls/


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def f(x):
            cnt = 1
            last_pos = position[0]
            for pos in position:
                if pos - last_pos >= x:
                    cnt += 1
                    last_pos = pos

            return cnt

        position.sort()
        left = 0
        right = position[-1]
        answer = 0
        while left <= right:
            mid = (left + right) // 2

            if f(mid) >= m:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer
