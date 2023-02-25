# https://programmers.co.kr/learn/courses/30/lessons/60059


def rotate_90(m):
    N = len(m)
    result = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            result[c][N - 1 - r] = m[r][c]
    return result


def clearLock(lock, n, m):
    lock_field_length = n + (m * 2) - 2
    lock_field = [[0] * lock_field_length for _ in range(lock_field_length)]
    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            lock_field[i][j] = lock[i - m + 1][j - m + 1]
    return lock_field


def putKey(lock_field, key, r, c):
    for i in range(r, r + len(key)):
        for j in range(c, c + len(key)):
            if key[i - r][j - c] == 1:
                lock_field[i][j] += 1


def isSuccess(lock_field, n, m):
    for i in range(m - 1, n + m - 1):
        for j in range(m - 1, n + m - 1):
            if lock_field[i][j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    lock_field = clearLock(lock, n, m)

    for _ in range(4):
        key = rotate_90(key)
        for i in range(0, n + m - 1):
            for j in range(0, n + m - 1):
                putKey(lock_field, key, i, j)
                if isSuccess(lock_field, n, m):
                    return True
                lock_field = clearLock(lock, n, m)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
