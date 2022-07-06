# https://www.acmicpc.net/problem/12094
# 통과못함 : 시간초과

import sys
from collections import deque
from copy import deepcopy

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp_max_block = [0] * 11
answer = -1


def same(A, B):
    for i in range(n):
        for j in range(n):
            if A[i][j] != B[i][j]:
                return False
    return True


# up, down, left, right
def move(graph, dir):
    result = [[0] * n for _ in range(n)]

    if dir == 0:
        for j in range(n):
            temp = deque()
            for i in range(n):
                if graph[i][j]:
                    temp.append(graph[i][j])

            k = 0
            while temp:
                element = temp.popleft()
                if temp and temp[0] == element:
                    element <<= 1
                    temp.popleft()
                result[k][j] = element
                k += 1

    elif dir == 1:
        for j in range(n):
            temp = deque()
            for i in range(n - 1, -1, -1):
                if graph[i][j]:
                    temp.append(graph[i][j])

            k = n - 1
            while temp:
                element = temp.popleft()
                if temp and temp[0] == element:
                    element <<= 1
                    temp.popleft()
                result[k][j] = element
                k -= 1

    elif dir == 2:
        for i in range(n):
            temp = deque()
            for j in range(n):
                if graph[i][j]:
                    temp.append(graph[i][j])

            k = 0
            while temp:
                element = temp.popleft()
                if temp and temp[0] == element:
                    element <<= 1
                    temp.popleft()
                result[i][k] = element
                k += 1

    elif dir == 3:
        for i in range(n):
            temp = deque()
            for j in range(n - 1, -1, -1):
                if graph[i][j]:
                    temp.append(graph[i][j])

            k = n - 1
            while temp:
                element = temp.popleft()
                if temp and temp[0] == element:
                    element <<= 1
                    temp.popleft()
                result[i][k] = element
                k -= 1

    return result


def find_max_block(graph):
    maximum = -1
    for r in graph:
        maximum = max(max(r), maximum)
    return maximum


def simul(graph, depth=0):
    global answer
    max_block = find_max_block(graph)

    #
    if dp_max_block[depth] > max_block:
        return

    answer = max(answer, max_block)
    dp_max_block[depth] = max(dp_max_block[depth], max_block)

    if depth == 10:
        b = answer
        while depth > 0:
            dp_max_block[depth] = b
            b >>= 1
            depth -= 1
        return

    for i in range(4):
        copied = deepcopy(graph)
        copied = move(copied, i)
        if same(graph, copied):
            continue
        simul(copied, depth + 1)


simul(graph)
print(answer)
