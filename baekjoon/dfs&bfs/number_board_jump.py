# https://www.acmicpc.net/problem/2210

graph = []
for _ in range(5):
    graph.append(list(input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

candidate = set()


def dfs(x, y, pwd):
    pwd += graph[x][y]
    if len(pwd) == 6:
        candidate.add(pwd)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            dfs(nx, ny, pwd)


for i in range(5):
    for j in range(5):
        dfs(i, j, "")
print(len(candidate))
