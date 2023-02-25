# https://leetcode.com/problems/jump-game-iii/

from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        q = deque([start])
        visited = [0] * n
        visited[start] = 1
        while q:
            now = q.popleft()

            if arr[now] == 0:
                return True

            for _next in [now - arr[now], now + arr[now]]:
                if _next < 0 or _next >= n:
                    continue
                if visited[_next]:
                    continue

                q.append(_next)
                visited[_next] = 1

        return False
