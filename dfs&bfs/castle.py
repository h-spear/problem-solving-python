# https://www.acmicpc.net/problem/2234

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

# left, up, right, down
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
bit = [1, 2, 4, 8]

visited = [[0] * n for _ in range(m)]


def bfs(x, y, num):
    q = deque()
    visited[x][y] = num
    q.append((x, y))
    area = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            if graph[x][y] & bit[i]:
                continue

            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] & bit[(2 + i) % 4]:
                continue

            q.append((nx, ny))
            visited[nx][ny] = num
            area += 1
    return area


cnt = 1
area = []
room = []
for i in range(m):
    for j in range(n):
        if visited[i][j]:
            continue
        area.append(bfs(i, j, cnt))
        room.append((i, j))
        cnt += 1

contact = [set() for _ in range(cnt)]


def bfs_for_contact(x, y, num):
    q = deque([(x, y)])
    _visited = [[0] * n for _ in range(m)]
    _visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if _visited[nx][ny]:
                continue
            if visited[nx][ny] != num:
                contact[num].add(visited[nx][ny])
                continue
            _visited[nx][ny] = 1
            q.append((nx, ny))


for i, coord in enumerate(room):
    x, y = coord
    bfs_for_contact(x, y, i + 1)

max_after_crash_area = 0
for i in range(1, cnt):
    for x in list(contact[i]):
        max_after_crash_area = max(max_after_crash_area, area[i - 1] + area[x - 1])

print(cnt - 1)
print(max(area))
print(max_after_crash_area)
