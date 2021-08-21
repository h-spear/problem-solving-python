from collections import deque

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, -1, 1, -1, 1]

for tc in range(int(input())):

    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    def bfs(x, y):
        visited = [[False] * l for _ in range(l)]
        q = deque([(0, x, y)])
        visited[x][y] = True

        while q:
            cost, x, y = q.popleft()

            if x == target_x and y == target_y:
                return cost

            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= 0 and nx < l and ny >= 0 and ny < l:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((cost + 1, nx, ny))

    print(bfs(x, y))
