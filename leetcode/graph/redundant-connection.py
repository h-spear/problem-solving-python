# https://leetcode.com/problems/redundant-connection/


class Solution:
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, a, b):
        a = self.find(parent, a)
        b = self.find(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # kruskal
        answer = []
        parent = [i for i in range(1001)]
        for a, b in edges:
            if self.find(parent, a) == self.find(parent, b):
                answer = [a, b]
                continue

            self.union(parent, a, b)

        return answer
