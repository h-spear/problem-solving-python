# https://www.acmicpc.net/problem/1867
# Minimum Vertex Cover

from collections import defaultdict


def dfs(row):
    if visit[row]:
        return False
    visit[row] = True

    for col in graph[row]:
        if not match[col] or dfs(match[col]):
            match[col] = row
            return True
    return False


MAX_SIZE = 500
answer = 0
graph = defaultdict(list)  # row -> col
n, k = map(int, input().split())
visit = None
match = [0] * (MAX_SIZE + 1)
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)

# bipartite
for row in graph:
    visit = [False] * (MAX_SIZE + 1)
    if dfs(row):
        answer += 1

print(answer)
