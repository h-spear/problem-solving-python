# https://www.acmicpc.net/problem/3085

from copy import deepcopy

n = int(input())
graph = [list(input()) for _ in range(n)]


def find_longest(graph):
    longest = 0
    for i in range(n):
        now = graph[i][0]
        cnt = 0
        for j in range(n):
            if graph[i][j] == now:
                cnt += 1
            else:
                longest = max(longest, cnt)
                cnt = 1
                now = graph[i][j]
        longest = max(longest, cnt)

    for j in range(n):
        now = graph[0][j]
        cnt = 0
        for i in range(n):
            if graph[i][j] == now:
                cnt += 1
            else:
                longest = max(longest, cnt)
                cnt = 1
                now = graph[i][j]
        longest = max(longest, cnt)

    return longest


dx = [1, 0]
dy = [0, 1]


def solution():
    answer = 0
    for x in range(n):
        for y in range(n):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx >= n or ny >= n:
                    continue
                if graph[nx][ny] == graph[x][y]:
                    continue

                copy = deepcopy(graph)
                copy[x][y], copy[nx][ny] = copy[nx][ny], copy[x][y]
                answer = max(answer, find_longest(copy))
    return answer


print(solution())
