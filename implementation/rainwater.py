# https://www.acmicpc.net/problem/14719

from collections import deque


h, w = map(int, input().split())
block = list(map(int, input().split()))
answer = 0


def bfs(x, h, visited):
    global answer
    q = deque([x])
    visited[x] = 1
    flag = False
    temp = [x]
    while q:
        x = q.popleft()

        for dx in [-1, 1]:
            nx = x + dx

            if nx < 0 or nx >= w:
                flag = True
                continue
            if visited[nx]:
                continue
            if block[nx] > h:
                continue
            q.append(nx)
            temp.append(nx)
            visited[nx] = 1

    if flag:
        return 0
    else:
        for i in temp:
            block[i] += 1
        answer += len(temp)


def rainwater(h):
    visited = [0] * w
    for x in range(w):
        if visited[x]:
            continue
        if block[x] > h:
            continue
        bfs(x, h, visited)


def simulation():
    for i in range(h):
        rainwater(i)
    print(answer)


simulation()
