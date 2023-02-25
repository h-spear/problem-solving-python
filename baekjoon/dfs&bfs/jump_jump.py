# https://www.acmicpc.net/problem/14248

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stone = [0]
stone.extend(list(map(int, input().split())))
start = int(input())

visited = [0] * 100001
q = deque([start])
cnt = 1
visited[start] = 1

while q:
    x = q.popleft()
    jump = stone[x]

    for next in [x - jump, x + jump]:
        if next >= 1 and next <= n and not visited[next]:
            q.append(next)
            visited[next] = 1
            cnt += 1

print(cnt)
