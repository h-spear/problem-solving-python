# https://www.acmicpc.net/problem/17276

from typing import *


def rotate_degree45(array: List[List[int]]) -> List[List[int]]:
    i: int
    j: int
    k: int = n // 2
    rotated: List[List[int]] = [[0] * n for _ in range(n)]

    # 주대각선을 가운데열로 옮긴다.
    for i in range(n):
        rotated[i][k] = array[i][i]

    # 가운데열을 부대각선으로 옮긴다.
    for i in range(n):
        rotated[i][n - i - 1] = array[i][k]

    # 부대각선을 가운데행으로 옮긴다.
    for j in range(n - 1, -1, -1):
        rotated[k][j] = array[n - j - 1][j]

    # 가운데행을 주대각선으로 옮긴다.
    for j in range(n - 1, -1, -1):
        rotated[j][j] = array[k][j]

    for i in range(n):
        for j in range(n):
            if rotated[i][j] == 0:
                rotated[i][j] = array[i][j]

    return rotated


def rotate(array: List[List[int]], degree: int) -> List[List[int]]:
    degree = 360 + degree if degree < 0 else degree % 360
    rotate_count: int = degree // 45

    rotated: List[List[int]] = array
    for _ in range(rotate_count):
        rotated = rotate_degree45(rotated)

    return rotated


def print_2d_array(array: List[List[int]]) -> None:
    for i in range(n):
        print(*array[i])


t: int
n: int
d: int

t = int(input())

for tc in range(t):
    n, d = map(int, input().split())
    array: List[List[int]] = []

    for _ in range(n):
        array.append(list(map(int, input().split())))

    rotated = rotate(array, d)
    print_2d_array(rotated)
