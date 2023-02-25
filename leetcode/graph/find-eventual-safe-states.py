# https://leetcode.com/problems/find-eventual-safe-states/
# https://leetcode.com/problems/find-eventual-safe-states/discuss/2135423/Python-DFS-Solution


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminal_nodes = set()
        visited = set()
        n = len(graph)

        for i, nei in enumerate(graph):
            if not nei:
                terminal_nodes.add(i)

        def dfs(node):
            if node in terminal_nodes:
                return True
            if node in visited:
                return False

            visited.add(node)

            for nei in graph[node]:
                if dfs(nei) == False:
                    return False

            terminal_nodes.add(node)
            return True

        for i in range(n):
            if i in visited:
                continue
            dfs(i)

        return sorted(list(terminal_nodes))
