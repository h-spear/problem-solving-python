# https://school.programmers.co.kr/learn/courses/30/lessons/62050

from collections import deque, defaultdict

INF = float("inf")
gLand = None
gHeight = 0
visited = [[0] * (301) for _ in range(301)]
N = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_valid(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    return True


def bfs(x, y, num):
    visited[x][y] = num
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if abs(gLand[nx][ny] - gLand[x][y]) > gHeight:
                continue
            q.append((nx, ny))
            visited[nx][ny] = num


def make_edges():
    num = 0
    hash = defaultdict(lambda: INF)

    # grouping
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                num += 1
                bfs(i, j, num)

    # make hash
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not is_valid(nx, ny):
                    continue
                num1, num2 = visited[x][y], visited[nx][ny]
                diff = abs(gLand[nx][ny] - gLand[x][y])
                if num1 == num2:
                    continue
                if hash[(num1, num2)] <= diff:
                    continue
                hash[(num1, num2)] = diff
                hash[(num2, num1)] = diff

    return sorted([(c, a, b) for (a, b), c in hash.items()])


def solution(land, height):
    global gLand, gHeight, N
    gLand = land
    gHeight = height
    N = len(land)
    answer = 0

    # kruskal
    edges = make_edges()
    parent = [i for i in range(N * N + 1)]
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        union(parent, a, b)
        answer += c

    return answer
