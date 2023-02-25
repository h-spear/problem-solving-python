# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo = 0
        uo = len(height) - 1
        answer = 0
        while lo < uo:
            area = min(height[lo], height[uo]) * (uo - lo)
            answer = max(answer, area)

            if height[lo] < height[uo]:
                lo += 1
            else:
                uo -= 1

        return answer
