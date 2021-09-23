# https://www.acmicpc.net/problem/12761

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


a, b, n, m = map(int, input().split())

visited = [-1] * 100001
q = deque([n])
visited[n] = 0
while q:
    x = q.popleft()

    if x == m:
        print(visited[x])
        break

    for next in [x + 1, x - 1, x + a, x - a, x + b, x - b, x * a, x * b]:
        if next >= 0 and next <= 100000 and visited[next] == -1:
            q.append(next)
            visited[next] = visited[x] + 1
