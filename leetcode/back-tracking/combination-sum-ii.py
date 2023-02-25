# https://leetcode.com/problems/combination-sum-ii/

from collections import Counter


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []

        n = len(candidates)
        candidates.sort()
        visited = set()
        answer = []
        path = []

        def generate_key():
            counter = Counter(path)
            return tuple(counter.items())

        def dfs(idx):
            p = generate_key()
            if p in visited:
                return
            visited.add(p)

            summation = sum(path)
            if summation == target:
                answer.append(tuple(path[::]))
                return
            elif summation > target:
                return

            for i in range(idx + 1, n):
                path.append(candidates[i])
                dfs(i)
                path.pop()

        def handler():
            for i in range(n):
                path.append(candidates[i])
                dfs(i)
                path.pop()

        handler()
        return answer
