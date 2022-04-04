# https://www.acmicpc.net/problem/2344

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
hash = {}
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def extend_graph(graph):
    extended = [[0] * (m + 2) for _ in range(n + 2)]
    cnt = 1
    d = 0
    for i in range(1, n + 1):
        extended[i][0] = cnt
        hash[cnt] = (i, 0, d)
        cnt += 1

    d = 1
    for j in range(1, m + 1):
        extended[n + 1][j] = cnt
        hash[cnt] = (n + 1, j, d)
        cnt += 1

    d = 2
    for i in range(n, 0, -1):
        extended[i][m + 1] = cnt
        hash[cnt] = (i, m + 1, d)
        cnt += 1

    d = 3
    for j in range(m, 0, -1):
        extended[0][j] = cnt
        hash[cnt] = (0, j, d)
        cnt += 1

    for i in range(n):
        for j in range(m):
            extended[i + 1][j + 1] = graph[i][j]

    return extended


def shoot_light(graph, num):
    x, y, d = hash[num]

    x += dx[d]
    y += dy[d]
    while 1 <= x <= n and 1 <= y <= m:
        if graph[x][y] == 1:
            d = 1 - d if d <= 1 else 5 - d

        x += dx[d]
        y += dy[d]
    return graph[x][y]


def simulation(graph):
    graph = extend_graph(graph)
    answer = []
    for i in range(1, (n + m) * 2 + 1):
        answer.append(shoot_light(graph, i))

    print(*answer)


simulation(graph)
