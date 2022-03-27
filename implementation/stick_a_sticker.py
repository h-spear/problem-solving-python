# https://www.acmicpc.net/problem/18808

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    temp = []
    for i in range(r):
        temp.append(list(map(int, input().split())))
    stickers.append(temp)


def rotate_matrix_90(A):
    n = len(A)  # length of row
    m = len(A[0])  # length of column
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def is_possible(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            if sticker[i][j] == 1 and graph[i + x][j + y] == 1:
                return False
    return True


def stick_sticker(sticker, x, y):
    r, c = len(sticker), len(sticker[0])
    for i in range(r):
        for j in range(c):
            graph[x + i][y + j] = max(sticker[i][j], graph[x + i][y + j])


def search_and_stick(sticker):
    for rot in range(4):
        r, c = len(sticker), len(sticker[0])
        for i in range(n - r + 1):
            for j in range(m - c + 1):
                if is_possible(sticker, i, j):
                    stick_sticker(sticker, i, j)
                    return
        sticker = rotate_matrix_90(sticker)


def count_sticker_grid():
    cnt = 0
    for row in graph:
        cnt += sum(row)
    return cnt


def simulation():
    for sticker in stickers:
        search_and_stick(sticker)

    answer = count_sticker_grid()
    print(answer)


simulation()
