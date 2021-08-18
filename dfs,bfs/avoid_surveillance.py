# https://www.acmicpc.net/problem/18428

from itertools import combinations

n = int(input())
teachers = set()
students = set()
empty = set()
for i in range(n):
    input_data = list(input().split())
    for j in range(n):
        if input_data[j] == "S":
            students.add((i, j))
        elif input_data[j] == "T":
            teachers.add((i, j))
        elif input_data[j] == "X":
            empty.add((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def serveiling(graph, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == "O":
                break
            elif graph[nx][ny] == "X":
                graph[nx][ny] = "T"

            nx = nx + dx[i]
            ny = ny + dy[i]


def makeField(objects):
    graph = [["X"] * n for _ in range(n)]
    for x, y in teachers:
        graph[x][y] = "T"
    for x, y in objects:
        graph[x][y] = "O"
    return graph


def isAvoidable(graph):
    for x, y in students:
        if graph[x][y] == "T":
            return False
    return True


answer = "NO"
# simulation
for object_case in combinations(empty, 3):
    field_to_simulate = makeField(object_case)
    for x, y in teachers:
        serveiling(field_to_simulate, x, y)

    if isAvoidable(field_to_simulate):
        answer = "YES"
        break

print(answer)
