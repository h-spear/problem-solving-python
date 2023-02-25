# https://www.acmicpc.net/problem/2188
# bipartite matching


def dfs(c):
    if visited[c]:
        return False
    visited[c] = True

    for i in cow[c]:
        if barns[i] == -1 or dfs(barns[i]):
            barns[i] = c
            return True

    return False


answer = 0
n, m = map(int, input().split())
cow = [[] for _ in range(n)]
barns = [-1] * (m + 1)
for i in range(n):
    info = list(map(int, input().split()))
    cow[i] = info[1:]

for i in range(n):
    visited = [False] * n
    if dfs(i):
        answer += 1


print(answer)
