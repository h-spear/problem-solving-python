# https://leetcode.com/problems/trapping-rain-water/
# bfs 시간초과

from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        def bfs(x, h, visited):
            visited[x] = 1
            q = deque([x])
            flag = True
            water = 1
            while q:
                x = q.popleft()

                for dx in [-1, 1]:
                    nx = x + dx

                    if nx < 0 or nx >= w:
                        flag = False
                        continue
                    if visited[nx]:
                        continue
                    if height[nx] > h:
                        continue

                    q.append(nx)
                    visited[nx] = 1
                    water += 1

            if flag:
                return water
            else:
                return 0

        def rainwater(h):
            h_water = 0
            visited = [0] * w
            for i in range(w):
                if visited[i]:
                    continue
                if height[i] <= h:
                    h_water += bfs(i, h, visited)
            return h_water

        w = len(height)
        max_height = max(height)
        answer = 0
        for h in range(max_height):
            answer += rainwater(h)

        return answer
