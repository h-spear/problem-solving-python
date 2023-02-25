# https://leetcode.com/problems/keys-and-rooms/

from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [0] * n
        visited[0] = 1
        q = deque([0])
        while q:
            x = q.popleft()

            for y in rooms[x]:
                if visited[y]:
                    continue
                q.append(y)
                visited[y] = 1

        return 0 not in visited
