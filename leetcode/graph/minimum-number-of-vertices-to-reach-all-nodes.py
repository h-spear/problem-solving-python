# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# 1
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        visited = set()
        for _from, to in edges:
            visited.add(to)

        s = set(range(n))
        return list(s - visited)


# 2
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        in_degree = [0] * n

        for _from, to in edges:
            in_degree[to] += 1

        return [i for i in range(n) if in_degree[i] == 0]
