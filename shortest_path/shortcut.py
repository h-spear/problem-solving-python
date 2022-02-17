# https://www.acmicpc.net/problem/1446

from collections import defaultdict


n, d = map(int, input().split())
graph = defaultdict(list)
distance = [i for i in range(d + 1)]
for _ in range(n):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for i in range(0, d + 1):
    distance[i] = min(distance[i - 1] + 1, distance[i])
    for e, t in graph[i]:
        if e > d:
            continue
        if distance[e] > distance[i] + t:
            distance[e] = distance[i] + t

print(distance[d])
