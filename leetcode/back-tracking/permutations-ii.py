# https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [0] * n
        path = []
        answer = []
        s = set()

        def dfs(depth):
            if depth == n:
                s.add(tuple(path[::]))
                return

            for i in range(n):
                if visited[i]:
                    continue

                visited[i] = 1
                path.append(nums[i])
                dfs(depth + 1)
                visited[i] = 0
                path.pop()

        dfs(0)
        for candidate in s:
            answer.append(list(candidate))
        return answer
