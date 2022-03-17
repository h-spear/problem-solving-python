# https://www.acmicpc.net/problem/12100
# 0인 부분을 이동시키고 숫자 더하고, 다시 0인 부분을 이동시키는 방식으로 구현

from copy import deepcopy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def get_max(graph):
    res = 0
    for i in range(n):
        for j in range(n):
            res = max(graph[i][j], res)

    return res


def move_up(graph):
    def move_zero():
        for j in range(n):
            for i in range(n - 1):
                if graph[i][j] != 0:
                    continue
                k = i + 1
                while k < n and graph[k][j] == 0:
                    k += 1

                if k == n:
                    continue
                graph[i][j] = graph[k][j]
                graph[k][j] = 0

    move_zero()
    for j in range(n):
        for i in range(n - 1):
            if graph[i][j] == graph[i + 1][j]:
                graph[i][j] *= 2
                graph[i + 1][j] = 0
    move_zero()

    return graph


def move_down(graph):
    def move_zero():
        for j in range(n):
            for i in range(n - 1, 0, -1):
                if graph[i][j] != 0:
                    continue
                k = i - 1
                while k >= 0 and graph[k][j] == 0:
                    k -= 1

                if k == -1:
                    continue
                graph[i][j] = graph[k][j]
                graph[k][j] = 0

    move_zero()
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if graph[i][j] == graph[i - 1][j]:
                graph[i][j] *= 2
                graph[i - 1][j] = 0
    move_zero()

    return graph


def move_left(graph):
    def move_zero():
        for i in range(n):
            for j in range(n - 1):
                if graph[i][j] != 0:
                    continue
                k = j + 1
                while k < n and graph[i][k] == 0:
                    k += 1

                if k == n:
                    continue
                graph[i][j] = graph[i][k]
                graph[i][k] = 0

    move_zero()
    for i in range(n):
        for j in range(n - 1):
            if graph[i][j] == graph[i][j + 1]:
                graph[i][j] *= 2
                graph[i][j + 1] = 0
    move_zero()
    return graph


def move_right(graph):
    def move_zero():
        for i in range(n):
            for j in range(n - 1, 0, -1):
                if graph[i][j] != 0:
                    continue

                k = j - 1
                while k >= 0 and graph[i][k] == 0:
                    k -= 1

                if k == -1:
                    continue
                graph[i][j] = graph[i][k]
                graph[i][k] = 0

    move_zero()
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if graph[i][j] == graph[i][j - 1]:
                graph[i][j] *= 2
                graph[i][j - 1] = 0
    move_zero()

    return graph


def simulate(graph, cnt=0):
    global answer
    answer = max(answer, get_max(graph))
    if cnt == 5:
        return

    simulate(move_up(deepcopy(graph)), cnt + 1)
    simulate(move_down(deepcopy(graph)), cnt + 1)
    simulate(move_left(deepcopy(graph)), cnt + 1)
    simulate(move_right(deepcopy(graph)), cnt + 1)
    return


simulate(graph)
print(answer)
