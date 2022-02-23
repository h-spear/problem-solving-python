# https://programmers.co.kr/learn/courses/30/lessons/86052


def solution(grid):
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    n = len(grid)
    m = len(grid[0])
    visited = [[[0] * 4 for _ in range(m)] for _ in range(n)]

    def dfs(x, y, d):
        nx, ny, nd = x, y, d
        cnt = 0
        visited[x][y][d] = 1
        while 1:
            nx = (nx + dx[nd]) % n
            ny = (ny + dy[nd]) % m
            cnt += 1

            if grid[nx][ny] == "R":
                nd = (nd + 1) % 4
            elif grid[nx][ny] == "L":
                nd = (nd - 1) % 4

            if visited[nx][ny][nd]:
                if (nx, ny, nd) == (x, y, d):
                    return cnt
                else:
                    return 0
            visited[nx][ny][nd] = 1

    for x in range(n):
        for y in range(m):
            for d in range(4):
                if visited[x][y][d]:
                    continue
                res = dfs(x, y, d)
                if res != 0:
                    answer.append(res)

    return sorted(answer)
