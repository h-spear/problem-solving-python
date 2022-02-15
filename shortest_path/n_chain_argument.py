# https://www.acmicpc.net/problem/15723

n = int(input())
graph = [[0] * 26 for _ in range(26)]
for _ in range(n):
    p, q = input().split(" is ")
    p = ord(p) - ord("a")
    q = ord(q) - ord("a")
    graph[p][q] = 1

# floyd_warshall
for k in range(26):
    for i in range(26):
        for j in range(26):
            if i == j:
                continue
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

m = int(input())
for _ in range(m):
    p, q = input().split(" is ")
    p = ord(p) - ord("a")
    q = ord(q) - ord("a")
    print("T" if graph[p][q] else "F")
