# https://leetcode.com/problems/largest-perimeter-triangle/

from collections import deque


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def is_triangle(a, b, c):
            if a + b > c and b + c > a and c + a > b:
                return True
            return False

        nums.sort()
        q = deque()
        for _ in range(3):
            q.append(nums.pop())

        while nums:
            if is_triangle(*q):
                return sum(q)

            q.popleft()
            q.append(nums.pop())

        if is_triangle(*q):
            return sum(q)

        return 0
