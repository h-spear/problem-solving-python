# https://www.acmicpc.net/problem/12100
# deque를 사용하여 구현 220701

from collections import deque
from copy import deepcopy


n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

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
                    element *= 2
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
                    element *= 2
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
                    element *= 2
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
                    element *= 2
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
    answer = max(answer, find_max_block(graph))
    if depth == 5:
        return

    for i in range(4):
        copied = deepcopy(graph)
        copied = move(copied, i)
        simul(copied, depth + 1)


simul(graph)
print(answer)
