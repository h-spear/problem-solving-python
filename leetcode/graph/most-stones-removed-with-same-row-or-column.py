# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

from collections import deque, defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        hash_x = defaultdict(set)
        hash_y = defaultdict(set)

        for x, y in stones:
            hash_x[x].add((x, y))
            hash_y[y].add((x, y))

        visited = set()

        def bfs(x, y):
            cnt = 0
            q = deque()
            q.append((x, y))
            visited.add((x, y))
            while q:
                x, y = q.popleft()

                for nx, ny in hash_x[x]:
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    cnt += 1

                for nx, ny in hash_y[y]:
                    if (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    q.append((nx, ny))
                    cnt += 1

            return cnt

        answer = 0
        for x, y in stones:
            if (x, y) in visited:
                continue
            answer += bfs(x, y)

        return answer
