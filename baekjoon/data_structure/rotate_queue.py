# https://www.acmicpc.net/problem/1021

from collections import deque

n, m = map(int, input().split())
peek = list(map(int, input().split()))

q = deque([i for i in range(1, n + 1)])

cnt = 0
for p in peek:
    if q[0] == p:
        q.popleft()
    else:
        idx = q.index(p)
        if idx < len(q) - idx:
            while q[0] != p:
                q.append(q.popleft())
                cnt += 1
            q.popleft()
        else:
            while q[0] != p:
                q.appendleft(q.pop())
                cnt += 1
            q.popleft()

print(cnt)
