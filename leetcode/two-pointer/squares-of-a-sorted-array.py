# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        answer = []

        i = 0
        while i < n:
            num = nums[i]
            if num < 0:
                stack.append(num ** 2)
                i += 1
            else:
                break

        while i < n:
            temp = nums[i] ** 2
            while stack and stack[-1] <= temp:
                answer.append(stack.pop())
            answer.append(temp)
            i += 1

        while stack:
            answer.append(stack.pop())

        return answer
