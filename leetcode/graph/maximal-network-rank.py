# https://leetcode.com/problems/maximal-network-rank/

from itertools import combinations
from collections import defaultdict


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)

        answer = 0

        def get_rank(x, y):
            counter = set()
            for nx in graph[x]:
                counter.add((min(x, nx), max(x, nx)))

            for ny in graph[y]:
                counter.add((min(y, ny), max(y, ny)))
            return len(counter)

        for candidate in combinations(range(n), 2):
            x, y = candidate
            answer = max(answer, get_rank(x, y))

        return answer
