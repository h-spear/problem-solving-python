# https://www.acmicpc.net/problem/5014

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

floor, start, end, up, down = map(int, input().split())

visited = [-1] * (floor + 1)
visited[start] = 0
q = deque([start])

answer = -1
while q:
    x = q.popleft()

    if x == end:
        answer = visited[x]
        break

    for i in [up, -down]:
        next = x + i
        if next >= 1 and next <= floor and visited[next] == -1:
            visited[next] = visited[x] + 1
            q.append(next)

print("use the stairs" if answer == -1 else answer)
