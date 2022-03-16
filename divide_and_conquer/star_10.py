# https://www.acmicpc.net/problem/2447

n = int(input())
board = [[" "] * n for _ in range(n)]


def func(x, y, l):
    if l == 1:
        board[x][y] = "*"
        return
    nn = l // 3
    func(x, y, nn)
    func(x, y + nn, nn)
    func(x, y + 2 * nn, nn)
    func(x + nn, y, nn)
    func(x + nn, y + 2 * nn, nn)
    func(x + 2 * nn, y, nn)
    func(x + 2 * nn, y + nn, nn)
    func(x + 2 * nn, y + 2 * nn, nn)


func(0, 0, n)

for x in board:
    print(*x, sep="")
