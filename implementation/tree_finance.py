# https://www.acmicpc.net/problem/16235
# heapq로는 시간초과, deque로 구현함
# 번식된 나무는 1살이므로 appendleft로 구현해야 함
# trees를 defaultdict로 구현하면 시간초과 (deque를 가진 이차원 배열로 구현함)

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
graph = [[5] * n for _ in range(n)]
dead = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
trees = [[deque() for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)


def one_year(day):
    breed = []
    for x in range(n):
        for y in range(n):
            if day != 0:
                # winter
                graph[x][y] += A[x][y]
                # summer
                graph[x][y] += dead[x][y]
                dead[x][y] = 0

            # spring
            for _ in range(len(trees[x][y])):
                age = trees[x][y].popleft()
                if graph[x][y] >= age:
                    graph[x][y] -= age
                    trees[x][y].append(age + 1)
                    if (age + 1) % 5 == 0:
                        breed.append((x, y))
                else:
                    dead[x][y] += age // 2

    # autumn
    for x, y in breed:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            trees[nx][ny].appendleft(1)


def spend_four_seasons(k):
    for day in range(k):
        one_year(day)


def count_tree(trees):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += len(trees[i][j])

    return cnt


spend_four_seasons(k)
print(count_tree(trees))
