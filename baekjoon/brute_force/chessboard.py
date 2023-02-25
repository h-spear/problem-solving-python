n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "B":
            graph[i][j] = 1
        else:
            graph[i][j] = -1


def check(graph, color):
    now = color
    cnt = 0
    for i in range(8):
        for j in range(8):
            if graph[i][j] != now:
                cnt += 1
            now *= -1
        now *= -1

    return cnt


def copy(graph, a, b):
    copy = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            copy[i][j] = graph[i + a][j + b]

    return copy


def solution():
    answer = 100
    for i in range(0, n - 7):
        for j in range(0, m - 7):
            copy_graph = copy(graph, i, j)
            answer = min(answer, check(copy_graph, 1), check(copy_graph, -1))

    print(answer)


solution()
