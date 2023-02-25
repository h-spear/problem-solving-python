# https://leetcode.com/problems/jump-game/

# O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        lastIndex = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i

        if lastIndex == 0:
            return True
        return False


# O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False for i in range(0, len(nums))]
        n = len(nums)
        lastIndex = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= lastIndex:
                dp[i] = True
                lastIndex = i

        return dp[0]


# O(n^2)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [0] * n
        visited[0] = 1

        for idx, num in enumerate(nums):
            if not visited[idx]:
                continue
            if idx + num >= n - 1:
                return True

            for i in range(num + 1):
                if idx + i >= n:
                    break
                visited[idx + i] = 1

        return visited[n - 1] == 1
