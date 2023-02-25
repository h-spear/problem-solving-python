# https://leetcode.com/problems/combinations/


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


# library
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))
