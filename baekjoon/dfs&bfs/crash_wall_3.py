# https://www.acmicpc.net/problem/16933
# 매우 어렵, 참고 : https://dailymapins.tistory.com/171
# 날짜를 4차원 배열이 아니라 따로 관리(for 문 len(q)) -> 시간을 더 줄일 수 있음

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0 : 낮, 1 : 밤
def bfs(x, y, tx, ty):
    q = deque([(x, y, 0)])
    day = 1
    while q:
        night = False if day > 0 else True
        for _ in range(len(q)):
            x, y, crash = q.popleft()
            today = abs(day)

            if x == tx - 1 and y == ty - 1:
                return today

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if visited[nx][ny][crash]:
                    continue

                if graph[nx][ny] == 0:
                    visited[nx][ny][crash] = today + 1
                    q.append((nx, ny, crash))
                elif (
                    crash < k and graph[nx][ny] == 1 and not visited[nx][ny][crash + 1]
                ):
                    if night:
                        q.append((x, y, crash))
                    else:
                        visited[nx][ny][crash + 1] = today + 1
                        q.append((nx, ny, crash + 1))
        day = day + 1 if day > 0 else day - 1
        day *= -1

    return -1


print(bfs(0, 0, n, m))
