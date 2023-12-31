# https://www.acmicpc.net/problem/1068

n = int(input())
graph = [[] for _ in range(n)]
parent = list(map(int, input().split()))
root = 0
for i, x in enumerate(parent):
    if x == -1:
        root = i
        continue
    graph[x].append(i)
removed = int(input())
visited = [0] * (n + 1)
answer = 0


def dfs(x):
    global answer
    visited[x] = 1
    if x == removed:
        return
    if len(graph[x]) == 0:
        answer += 1
        return

    for next in graph[x]:
        if visited[next]:
            continue
        if next == removed:
            # 삭제되는 노드들이 직선일 때 처리
            if len(graph[x]) > 1:
                continue
            answer += 1
            continue
        dfs(next)


dfs(root)
print(answer)
