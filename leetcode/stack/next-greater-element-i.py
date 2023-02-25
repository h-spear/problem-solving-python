# https://leetcode.com/problems/next-greater-element-i/


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        _hash = dict()
        stack = []
        answer = []

        for num in nums2:
            if not stack:
                stack.append(num)
                continue

            while stack and num > stack[-1]:
                item = stack.pop()
                _hash[item] = num

            stack.append(num)

        while stack:
            item = stack.pop()
            _hash[item] = -1

        for num in nums1:
            answer.append(_hash[num])

        return answer
