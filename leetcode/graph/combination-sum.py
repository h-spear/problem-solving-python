# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(path=[], idx=0):
            _sum = sum(path)
            if _sum > target:
                return
            if _sum == target:
                answer.append(path[:])
                return

            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                dfs(path, i)
                path.pop()

        dfs()
        return list(answer)
