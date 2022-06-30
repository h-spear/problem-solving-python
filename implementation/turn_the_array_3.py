# https://www.acmicpc.net/problem/16935


def flip_vertical(A):
    A.reverse()
    return A


def flip_horizontal(A):
    n = len(A)
    m = len(A[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][j] = A[i][m - j - 1]
    return result


def rotate_right(A):
    n = len(A)
    m = len(A[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = A[i][j]
    return result


def rotate_left(A):
    n = len(A)
    m = len(A[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = A[i][j]
    return result


def rotate_subarray_right(A):
    n = len(A)
    m = len(A[0])
    ln = n // 2
    lm = m // 2
    result = [[0] * m for _ in range(n)]
    for i in range(0, ln):
        for j in range(0, lm):
            result[i][j + lm] = A[i][j]

    for i in range(0, ln):
        for j in range(lm, m):
            result[i + ln][j] = A[i][j]

    for i in range(ln, n):
        for j in range(lm, m):
            result[i][j - lm] = A[i][j]

    for i in range(ln, n):
        for j in range(0, lm):
            result[i - ln][j] = A[i][j]

    return result


def rotate_subarray_left(A):
    n = len(A)
    m = len(A[0])
    ln = n // 2
    lm = m // 2
    result = [[0] * m for _ in range(n)]
    for i in range(0, ln):
        for j in range(0, lm):
            result[i + ln][j] = A[i][j]

    for i in range(0, ln):
        for j in range(lm, m):
            result[i][j - lm] = A[i][j]

    for i in range(ln, n):
        for j in range(lm, m):
            result[i - ln][j] = A[i][j]

    for i in range(ln, n):
        for j in range(0, lm):
            result[i][j + lm] = A[i][j]

    return result


def operation(A, op):
    if op == 1:
        A = flip_vertical(A)
    elif op == 2:
        A = flip_horizontal(A)
    elif op == 3:
        A = rotate_right(A)
    elif op == 4:
        A = rotate_left(A)
    elif op == 5:
        A = rotate_subarray_right(A)
    elif op == 6:
        A = rotate_subarray_left(A)
    return A


def print_array(A):
    for x in A:
        print(*x)


if __name__ == "__main__":
    n, m, r = map(int, input().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))
    ops = list(map(int, input().split()))

    for op in ops:
        A = operation(A, op)

    print_array(A)
