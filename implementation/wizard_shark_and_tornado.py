# https://www.acmicpc.net/problem/20057

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dx_ten = [-1]
dy_ten = [-1]


def tornado(x, y, graph, dir):
    sand = graph[x][y]
    out = 0

    one = int(sand * 0.01)
    two = int(sand * 0.02)
    five = int(sand * 0.05)
    seven = int(sand * 0.07)
    ten = int(sand * 0.1)
    alpha = sand - (one + two + seven + ten) * 2 - five

    if 0 <= x + dx[(dir + 1) % 4] < n and 0 <= y + dy[(dir + 1) % 4] < n:
        graph[x + dx[(dir + 1) % 4]][y + dy[(dir + 1) % 4]] += seven
    else:
        out += seven

    if 0 <= x + dx[dir - 1] < n and 0 <= y + dy[dir - 1] < n:
        graph[x + dx[dir - 1]][y + dy[dir - 1]] += seven
    else:
        out += seven

    if 0 <= x + 2 * dx[(dir + 1) % 4] < n and 0 <= y + 2 * dy[(dir + 1) % 4] < n:
        graph[x + 2 * dx[(dir + 1) % 4]][y + 2 * dy[(dir + 1) % 4]] += two
    else:
        out += two

    if 0 <= x + 2 * dx[dir - 1] < n and 0 <= y + 2 * dy[dir - 1] < n:
        graph[x + 2 * dx[dir - 1]][y + 2 * dy[dir - 1]] += two
    else:
        out += two

    if 0 <= x + dx[dir] + dy[dir] < n and 0 <= y + dx[dir] + dy[dir] < n:
        graph[x + dx[dir] + dy[dir]][y + dx[dir] + dy[dir]] += ten
    else:
        out += ten

    if 0 <= x + dx[dir] - dy[dir] < n and 0 <= y - dx[dir] + dy[dir] < n:
        graph[x + dx[dir] - dy[dir]][y - dx[dir] + dy[dir]] += ten
    else:
        out += ten

    if 0 <= x - dx[dir] + dy[dir] < n and 0 <= y + dx[dir] - dy[dir] < n:
        graph[x - dx[dir] + dy[dir]][y + dx[dir] - dy[dir]] += one
    else:
        out += one

    if 0 <= x - dx[dir] - dy[dir] < n and 0 <= y - dx[dir] - dy[dir] < n:
        graph[x - dx[dir] - dy[dir]][y - dx[dir] - dy[dir]] += one
    else:
        out += one

    if 0 <= x + 2 * dx[dir] < n and 0 <= y + 2 * dy[dir] < n:
        graph[x + 2 * dx[dir]][y + 2 * dy[dir]] += five
    else:
        out += five

    if 0 <= x + dx[dir] < n and 0 <= y + dy[dir] < n:
        graph[x + dx[dir]][y + dy[dir]] += alpha
    else:
        out += alpha

    graph[x][y] = 0
    return out


def simul(graph, n):
    x = y = n // 2
    dir = 0
    leng = 1
    cnt = 0
    answer = 0

    while 1:

        for l in range(leng):
            x = x + dx[dir]
            y = y + dy[dir]
            answer += tornado(x, y, graph, dir)
            if x == 0 and y == 0:
                print(answer)
                return

        cnt += 1
        dir = (dir + 1) % 4
        if cnt == 2:
            cnt = 0
            leng += 1


simul(graph, n)
