# https://www.acmicpc.net/problem/1298

from collections import defaultdict


def dfs(person):
    if visit[person]:
        return False
    visit[person] = True

    for candidate in graph[person]:
        if not notebook[candidate] or dfs(notebook[candidate]):
            notebook[candidate] = person
            return True

    return False


MAX_NOTEBOOK_NUMBER = 5000
n, m = map(int, input().split())
graph = defaultdict(list)
answer = 0
visit = None
notebook = [0] * (MAX_NOTEBOOK_NUMBER + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

for i in range(1, n + 1):
    visit = [0] * (n + 1)
    if dfs(i):
        answer += 1

print(answer)
