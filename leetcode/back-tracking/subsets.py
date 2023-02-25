# https://leetcode.com/problems/subsets/

# 1
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = [[]]
        path = []

        def dfs(idx):
            answer.append(path.copy())

            for i in range(idx + 1, n):
                path.append(nums[i])
                dfs(i)
                path.pop()

        def helper():
            for i in range(n):
                path.append(nums[i])
                dfs(i)
                path.pop()

        helper()
        return answer


# 2
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(path=[], idx=0):
            answer.append(path[:])

            for i in range(idx, len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(path, i + 1)
                path.pop()

        dfs()
        return answer
