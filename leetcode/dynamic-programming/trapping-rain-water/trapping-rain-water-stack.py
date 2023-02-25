# https://leetcode.com/problems/trapping-rain-water/
# https://leetcode.com/problems/trapping-rain-water/discuss/1374163/Python-Stack-O(N)-beats-99.99


class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        level = 0
        answer = 0

        for i, h in enumerate(height):
            while stack and h >= stack[-1][1]:
                last_i, last_h = stack.pop()
                answer += (last_h - level) * (i - last_i - 1)
                level = last_h

            if stack:
                answer += (h - level) * (i - stack[-1][0] - 1)

            if h:
                stack.append((i, h))

            level = 0

        return answer
