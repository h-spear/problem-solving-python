# https://www.acmicpc.net/problem/2563

paper = [[0] * 100 for _ in range(100)]


def stick_paper(x, y):
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1


def calc_area():
    cnt = 0
    for i in range(100):
        for j in range(100):
            if paper[i][j] == 1:
                cnt += 1
    return cnt


n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    stick_paper(x, y)

print(calc_area())
