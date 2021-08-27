# https://www.acmicpc.net/problem/18111

import sys
from collections import Counter

input = sys.stdin.readline

n, m, b = map(int, input().rstrip().split())
graph = []
for i in range(n):
    graph += map(int, input().rstrip().split())
graph = dict(Counter(graph))


def simulation(h):
    time = 0
    inven = 0
    for key in graph.keys():
        if key > h:
            time += 2 * graph[key] * (key - h)
            inven += graph[key] * (key - h)
        else:
            time += graph[key] * (h - key)
            inven -= graph[key] * (h - key)

    return time if inven + b >= 0 else -1


time = int(1e30)
height = 0
for h in range(max(graph), -1, -1):
    simulated = simulation(h)
    if simulated == -1:
        continue

    if time > simulated:
        time = simulated
        height = h

print(time, height)
