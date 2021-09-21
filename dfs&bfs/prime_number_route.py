# https://www.acmicpc.net/problem/1963

import math
from collections import deque

A = [True for i in range(10001)]

A[0], A[1] = False, False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(10000) + 1)):
    if A[i] == True:
        # i가 소수인 경우 i를 제외한 i의 모든 배수 false
        j = 2
        while i * j <= 10000:
            A[i * j] = False
            j += 1


def bfs(a, b):
    visited = [-1] * 10001
    q = deque([a])
    visited[a] = 0

    while q:
        x = q.popleft()

        if x == b:
            return visited[x]

        for i in range(4):
            for j in range(10):
                changed = list(str(x))
                changed[i] = str(j)
                changed = int("".join(changed))
                if visited[changed] == -1 and changed >= 1000 and A[changed]:
                    q.append(changed)
                    visited[changed] = visited[x] + 1


for tc in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))
