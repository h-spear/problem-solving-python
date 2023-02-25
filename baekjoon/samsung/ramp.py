# https://www.acmicpc.net/problem/14890


def rotate_degree_270(graph):
    n = len(graph)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[i][j] = graph[j][n - i - 1]

    return rotated


def simul(graph):
    global cnt

    n = len(graph)

    for i in range(n):
        used = [0] * n
        flag = False
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1]:
                continue
            if abs(graph[i][j] - graph[i][j + 1]) >= 2:
                flag = True
                break

            if graph[i][j] > graph[i][j + 1]:  # 내리막
                if j + l >= n:  # 길이 부족
                    flag = True
                    break

                if used[j + 1]:
                    flag = True
                    break

                used[j + 1] = 1
                for k in range(1, l):
                    if used[j + 1 + k]:
                        flag = True
                        break
                    if graph[i][j + 1] != graph[i][j + 1 + k]:
                        flag = True
                        break
                    used[j + 1 + k] = 1
            else:
                if j - l + 1 < 0:
                    flag = True
                    break

                if used[j]:
                    flag = True
                    break

                used[j] = 1
                for k in range(1, l):
                    if used[j - k]:
                        flag = True
                        break
                    if graph[i][j] != graph[i][j - k]:
                        flag = True
                        break
                    used[j - k] = 1

            if flag:
                break

        if not flag:
            cnt += 1


n, l = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt = 0

simul(graph)
graph = rotate_degree_270(graph)
simul(graph)

print(cnt)
