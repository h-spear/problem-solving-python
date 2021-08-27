# https://www.acmicpc.net/problem/16928

import heapq

n, m = map(int, input().split())

ladder = dict()
ladder_set = set()
snake = dict()
snake_set = set()

for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
    ladder_set.add(a)

for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b
    snake_set.add(a)


def bfs():
    heap = []
    heapq.heappush(heap, (0, 1))
    visited = [False] * 101

    while heap:
        cnt, x = heapq.heappop(heap)
        if x == 100:
            print(cnt)
            break
        if x in ladder_set:
            x = ladder[x]
        if x in snake_set:
            x = snake[x]

        for i in range(1, 7):
            if (x + i) <= 100 and visited[x + i] == False:
                visited[x + i] = True
                heapq.heappush(heap, (cnt + 1, x + i))


bfs()
