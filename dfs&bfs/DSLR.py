# https://www.acmicpc.net/problem/9019
# pypy3

from collections import deque
import sys

input = sys.stdin.readline


def bfs(n, m):
    visited = [False] * 10000
    q = deque([("", n)])
    visited[n] = True

    while q:
        cmd, now = q.popleft()

        if now == m:
            return cmd

        D = now * 2 % 10000
        if visited[D] == False:
            visited[D] = True
            q.append((cmd + "D", D))

        S = (now + 9999) % 10000
        if visited[S] == False:
            visited[S] = True
            q.append((cmd + "S", S))

        L = (now % 1000 * 10) + (now // 1000)
        if visited[L] == False:
            visited[L] = True
            q.append((cmd + "L", L))

        R = (now // 10) + (now % 10 * 1000)
        if visited[R] == False:
            visited[R] = True
            q.append((cmd + "R", R))


for _ in range(int(input())):
    n, m = map(int, input().rstrip().split())
    print(bfs(n, m))
