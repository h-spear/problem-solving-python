# https://leetcode.com/problems/next-greater-element-ii/
# Runtime: 193 ms, faster than 99.61% of Python3 online submissions for Next Greater Element II.


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        answer = [-1] * n
        nums += nums
        for i, num in enumerate(nums):
            if not stack:
                stack.append(i)
            elif nums[stack[-1]] >= num:
                stack.append(i)
            else:
                while stack and nums[stack[-1]] < num:
                    idx = stack.pop()
                    if idx < n:
                        answer[idx] = num
                stack.append(i)

        return answer
