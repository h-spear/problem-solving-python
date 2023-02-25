# https://www.acmicpc.net/problem/10994

n = int(input())
n = 4 * (n - 1) + 1

graph = [[" "] * n for _ in range(n)]
curr = 0
while curr <= n // 2:
    for i in range(curr, n - curr):
        graph[i][curr] = "*"
        graph[i][n - curr - 1] = "*"
        graph[curr][i] = "*"
        graph[n - curr - 1][i] = "*"
    curr = curr + 2

for row in graph:
    print("".join(row))
