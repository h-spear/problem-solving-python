# https://leetcode.com/problems/number-of-operations-to-make-network-connected/
# kruskal


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, a, b):
            a = find(parent, a)
            b = find(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        parent = [i for i in range(n)]
        redundancy_cable = 0
        disconnected_count = -1

        for x, y in connections:
            if find(parent, x) == find(parent, y):
                redundancy_cable += 1
            else:
                union(parent, x, y)

        for i in range(n):
            if parent[i] == i:
                disconnected_count += 1

        if redundancy_cable >= disconnected_count:
            return disconnected_count
        return -1
