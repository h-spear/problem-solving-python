# https://leetcode.com/problems/trapping-rain-water/
# dp
# 왼쪽, 오른쪽으로 각각 높이를 저장해둠
# -> 각 x좌표에서 물을 채울 수 있는 최대 높이를 바로 찾을 수 있음


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        to_right = [0] * n
        to_left = [0] * n
        to_right[0] = height[0]
        to_left[n - 1] = height[n - 1]

        for i in range(1, n):
            to_right[i] = max(height[i], to_right[i - 1])

        for i in range(n - 2, -1, -1):
            to_left[i] = max(height[i], to_left[i + 1])

        answer = 0
        for i in range(n):
            answer += min(to_right[i], to_left[i]) - height[i]

        return answer
