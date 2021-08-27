# https://www.acmicpc.net/problem/1992

import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))


def check(x, y, n):
    cnt = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] == 1:
                cnt += 1

    if cnt == n * n:
        return "1"
    elif cnt == 0:
        return "0"
    else:
        return -1


result = []


def dfs(x, y, n):
    checked = check(x, y, n)
    if checked == -1:
        result.append("(")
        dfs(x, y, n // 2)
        dfs(x, y + n // 2, n // 2)
        dfs(x + n // 2, y, n // 2)
        dfs(x + n // 2, y + n // 2, n // 2)
        result.append(")")
    else:
        result.append(checked)


dfs(0, 0, len(graph))
print("".join(result))
