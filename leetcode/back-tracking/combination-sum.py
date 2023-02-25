# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        s = set()
        path = []
        answer = []

        def dfs(idx, curr):
            if curr == target:
                s.add(tuple(path[::]))
                return
            elif curr > target:
                return

            for i in range(idx, n):
                path.append(candidates[i])
                dfs(i, curr + candidates[i])
                path.pop()

        dfs(0, 0)
        for c in s:
            answer.append(list(c))
        return answer
