# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]


# 상, 하, 좌, 우
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(r, c):
    visited[r][c] = True

    for d in dir:
        dr = r + d[0]
        dc = c + d[1]
        if dr >= 0 and dr < n and dc >= 0 and dc < m:
            if visited[dr][dc] == False and graph[dr][dc] == 0:
                dfs(dr, dc)


count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == False:
            dfs(i, j)
            count += 1

print(count)
