# https://school.programmers.co.kr/learn/courses/30/lessons/154540

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] * m for _ in range(n)]

    def bfs(x, y, visited):
        q = deque([(x, y)])
        visited[x][y] = 1
        res = 0

        while q:
            x, y = q.popleft()
            res += int(maps[x][y])

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] == "X":
                    continue

                q.append((nx, ny))
                visited[nx][ny] = 1
        return res

    answer = []
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            if maps[i][j] == "X":
                continue
            answer.append(bfs(i, j, visited))

    if not answer:
        return [-1]

    answer.sort()
    return answer
