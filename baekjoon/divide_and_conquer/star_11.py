# https://www.acmicpc.net/problem/2448

n = int(input())
result = [[" "] * (n * 2) for _ in range(n)]


def fn(x, y, n):
    if n == 3:
        result[x][y] = "*"
        result[x + 1][y - 1] = "*"
        result[x + 1][y + 1] = "*"
        for i in range(-2, 3):
            result[x + 2][y - i] = "*"
    else:
        nn = n // 2
        fn(x, y, nn)
        fn(x + nn, y - nn, nn)
        fn(x + nn, y + nn, nn)


fn(0, n - 1, n)
for x in result:
    print(*x, sep="")
