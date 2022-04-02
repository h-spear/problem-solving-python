# https://www.acmicpc.net/problem/15685
# curve의 규칙을 찾는 것이 어려웠음
# 참고 : https://tmdrl5779.tistory.com/146
n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(n):
    y, x, d, g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    for i in range(g):
        for j in range(len(curve) - 1, -1, -1):
            curve.append((curve[j] + 1) % 4)

    for d in curve:
        x += dx[d]
        y += dy[d]
        if x < 0 or x >= 101 or y < 0 or y >= 101:
            continue
        graph[x][y] = 1


answer = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i + 1][j] and graph[i][j + 1] and graph[i + 1][j + 1]:
            answer += 1
print(answer)
