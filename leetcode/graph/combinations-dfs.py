# https://leetcode.com/problems/combinations/

# 비효율적
class 비효율적tion:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(path, i):
            if i == k:
                answer.append(path)
                return

            for next in range(i + 1, n + 1):
                _path = path[:]
                if _path and next <= _path[-1]:
                    continue
                _path.append(next)
                dfs(_path, i + 1)

        dfs([], 0)
        return answer


# 효율적
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []

        def dfs(elements, start, k):
            if k == 0:
                answer.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return answer


# itertools 매우 빠름
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
