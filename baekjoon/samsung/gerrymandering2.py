# https://www.acmicpc.net/problem/17779

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = float("inf")


def divide_ward(x, y, d1, d2):
    ward = [[0] * n for _ in range(n)]

    for i in range(d1 + 1):
        ward[x + i][y - i] = 5
    for i in range(d2 + 1):
        ward[x + i][y + i] = 5
    for i in range(d2 + 1):
        ward[x + d1 + i][y - d1 + i] = 5
    for i in range(d1 + 1):
        ward[x + d2 + i][y + d2 - i] = 5

    for r in range(n):
        if sum(ward[r]) <= 5:
            continue
        five = False
        for c in range(n):
            if ward[r][c] == 5:
                five = True
            j = c + 1
            if five:
                while ward[r][j] != 5:
                    ward[r][j] = 5
                    j += 1
                break

    for r in range(n):
        for c in range(n):
            if ward[r][c] == 5:
                continue
            if (0 <= r < x + d1) and (0 <= c <= y):
                ward[r][c] = 1
            elif (0 <= r <= x + d2) and (y < c <= n - 1):
                ward[r][c] = 2
            elif (x + d1 <= r <= n - 1) and (0 <= c < y - d1 + d2):
                ward[r][c] = 3
            elif (x + d2 < r <= n - 1) and (y - d1 + d2 <= c <= n - 1):
                ward[r][c] = 4

    return ward


def calculate(x, y, d1, d2):
    global answer
    ward = divide_ward(x, y, d1, d2)
    population = [0] * 5
    for r in range(n):
        for c in range(n):
            population[ward[r][c] - 1] += graph[r][c]
    diff = max(population) - min(population)
    answer = min(answer, diff)


def simulate():
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    if x + 1 + d1 + d2 > n:
                        continue
                    if y + 1 + d2 > n:
                        continue
                    if y + 1 - d1 < 1:
                        continue
                    calculate(x, y, d1, d2)


simulate()
print(answer)
