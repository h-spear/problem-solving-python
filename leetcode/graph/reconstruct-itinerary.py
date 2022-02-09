# https://leetcode.com/problems/reconstruct-itinerary/

from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        graph = defaultdict(list)

        for a, b in tickets:
            graph[a].append(b)
        for a in graph:
            graph[a].sort(reverse=True)

        answer = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            answer.append(a)

        dfs("JFK")
        return answer[::-1]
