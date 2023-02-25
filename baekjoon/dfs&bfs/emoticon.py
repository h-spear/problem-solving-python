# https://www.acmicpc.net/problem/14226
# visited를 이중으로 체크

from collections import deque

n = int(input())

visited = [[0] * 3000 for _ in range(3000)]

q = deque([(1, 0, 0)])
visited[1][0] = 1
while q:
    s, clipboard, time = q.popleft()

    if s == n:
        print(time)
        break

    if not visited[s][s]:
        q.append((s, s, time + 1))
        visited[s][s] = 1
    if (
        s + clipboard <= 1001
        and clipboard != 0
        and not visited[s + clipboard][clipboard]
    ):
        q.append((s + clipboard, clipboard, time + 1))
        visited[s + clipboard][clipboard] = 1
    if s - 1 >= 0 and not visited[s - 1][clipboard]:
        q.append((s - 1, clipboard, time + 1))
        visited[s - 1][clipboard] = 1
