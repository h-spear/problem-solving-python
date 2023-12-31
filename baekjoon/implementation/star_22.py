# https://www.acmicpc.net/problem/10997

n = int(input())

if n == 1:
    print("*")
    exit(0)

c = 4 * (n - 1) + 1
r = c + 2
graph = [[" "] * c for _ in range(r)]


def is_valid(x, y):
    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    return True


left, right, top, bottom = 0, c - 1, 0, r - 1
while left <= right and top <= bottom:
    for j in range(right + 1, left - 1, -1):
        if is_valid(top, j):
            graph[top][j] = "*"
    top += 2

    for i in range(top - 1, bottom + 1):
        if is_valid(i, left):
            graph[i][left] = "*"
    left += 2

    for j in range(left - 1, right + 1):
        if is_valid(bottom, j):
            graph[bottom][j] = "*"
    bottom -= 2

    for i in range(bottom + 1, top - 1, -1):
        if is_valid(i, right):
            graph[i][right] = "*"
    right -= 2

for i, x in enumerate(graph):
    if i == 1:
        print("*")
    else:
        print("".join(x))
