# https://www.acmicpc.net/problem/10451

import sys

input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    data = list(map(int, input().split()))
    visited = [0] * (n + 1)

    for i in range(1, len(data) + 1):
        graph[i].append(data[i - 1])

    def visit(x):
        if visited[x] == 1:
            return 0
        while visited[x] == 0:
            visited[x] = 1
            x = graph[x][0]
        return 1

    answer = 0
    for i in range(1, n + 1):
        answer += visit(i)

    print(answer)
