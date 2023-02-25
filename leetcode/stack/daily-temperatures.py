# https://leetcode.com/problems/daily-temperatures/


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                j, t = stack.pop()
                answer[j] = i - j
            stack.append((i, temperature))

        return answer
