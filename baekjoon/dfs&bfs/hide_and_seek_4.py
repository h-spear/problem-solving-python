# https://www.acmicpc.net/problem/13913

from collections import deque

n, k = map(int, input().split())


def bfs(x):
    q = deque([(0, x)])
    visited = [-1] * (100001)
    visited[x] = 0
    answer = []
    while q:
        time, x = q.popleft()
        if x == k:
            answer.append(x)
            while x != n:
                x = visited[x]
                answer.append(x)
            answer.reverse()
            print(time)
            for x in answer:
                print(x, end=" ")

        if x + 1 <= 100000 and visited[x + 1] == -1:
            q.append((time + 1, x + 1))
            visited[x + 1] = x
        if x - 1 >= 0 and visited[x - 1] == -1:
            visited[x - 1] = x
            q.append((time + 1, x - 1))
        if 2 * x <= 100000 and visited[2 * x] == -1:
            visited[2 * x] = x
            q.append((time + 1, 2 * x))


bfs(n)
