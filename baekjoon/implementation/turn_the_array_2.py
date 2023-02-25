# https://www.acmicpc.net/problem/16927

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def rotate_array(A, r):
    temp = deque()
    x = 0
    y = 0
    l = min(n, m) // 2
    for c in range(l):
        for j in range(0 + c, m - c):
            temp.append(A[x + c][j])

        for i in range(1 + c, n - c):
            temp.append(A[i][m - 1 - c])

        for j in range(m - 2 - c, -1 + c, -1):
            temp.append(A[n - 1 - c][j])

        for i in range(n - 2 - c, 0 + c, -1):
            temp.append(A[i][y + c])

        mod = len(temp)
        rot = r % mod
        for _ in range(rot):
            temp.append(temp.popleft())

        for j in range(0 + c, m - c):
            A[x + c][j] = temp.popleft()

        for i in range(1 + c, n - c):
            A[i][m - 1 - c] = temp.popleft()

        for j in range(m - 2 - c, -1 + c, -1):
            A[n - 1 - c][j] = temp.popleft()

        for i in range(n - 2 - c, 0 + c, -1):
            A[i][y + c] = temp.popleft()


def print_array(A):
    for r in A:
        print(*r)


if __name__ == "__main__":
    n, m, r = map(int, input().split())
    A = []
    for _ in range(n):
        A.append(list(map(int, input().split())))

    rotate_array(A, r)
    print_array(A)
