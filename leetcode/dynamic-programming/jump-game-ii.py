# 나의 풀이 bfs: 4823ms
from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        q = deque([0])
        visited = [0] * n
        visited[0] = 1
        while q:
            x = q.popleft()

            if x == n - 1:
                return visited[x] - 1

            for i in range(1, nums[x] + 1):
                if x + i >= n:
                    continue
                if visited[x + i]:
                    continue
                q.append(x + i)
                visited[x + i] = visited[x] + 1

        return -1


# 참고: https://leetcode.com/problems/jump-game-ii/discuss/1725824/Python3-Runtime%3A-128-ms-faster-than-96.21-or-Memory%3A-15.1-MB-less-than-72.95
# 203ms


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        dp = [0] * n
        farthest = 0
        for i in range(1, n):
            while i > farthest + nums[farthest]:
                farthest += 1
            dp[i] = dp[farthest] + 1

        return dp[-1]


# recursion: 12205ms
class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def recursion(i):
            if i >= len(nums) - 1:
                return 0

            jumps = 123456

            for j in range(1, nums[i] + 1):
                jumps = min(jumps, 1 + recursion(i + j))

            return jumps

        return recursion(0)
