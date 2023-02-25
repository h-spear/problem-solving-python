# https://www.acmicpc.net/problem/12851

from collections import deque

n, k = map(int, input().split())


def bfs(x):
    q = deque([(0, x)])
    visited = [False] * (100001)
    answer = []

    while q:
        time, x = q.popleft()
        visited[x] = True
        if x == k:
            answer.append(time)

        if x + 1 <= 100000 and visited[x + 1] == False:
            q.append((time + 1, x + 1))
        if x - 1 >= 0 and visited[x - 1] == False:
            q.append((time + 1, x - 1))
        if 2 * x <= 100000 and visited[2 * x] == False:
            q.append((time + 1, 2 * x))

    print(min(answer))
    print(answer.count(min(answer)))


bfs(n)
