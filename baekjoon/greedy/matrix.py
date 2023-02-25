# https://www.acmicpc.net/problem/1080
# 참고 : https://velog.io/@dding_ji/baekjoon-1080

n, m = map(int, input().split())
graph = []
target = []
cnt = 0
for _ in range(n):
    graph.append(list(map(int, list(input()))))

for _ in range(n):
    target.append(list(map(int, list(input()))))


def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            graph[i][j] = 1 - graph[i][j]


def func():
    global cnt
    for i in range(n - 2):
        for j in range(m - 2):
            if graph[i][j] != target[i][j]:
                reverse(i, j)
                cnt += 1


def answer():
    for i in range(n):
        for j in range(m):
            if graph[i][j] != target[i][j]:
                print(-1)
                return
    print(cnt)


func()
answer()
