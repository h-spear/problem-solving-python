# https://www.acmicpc.net/problem/2342

import sys

sys.setrecursionlimit(100010)
n = -1
seq = None
cache = None


def move(now, next):
    if now == next:
        return 1
    if now == 0:
        return 2
    if abs(next - now) == 2:
        return 4
    return 3


def dfs(index, left, right):
    if index == n:
        return 0
    if cache[index][left][right] != -1:
        return cache[index][left][right]

    temp = 9876543210
    if right != seq[index]:
        temp = min(temp, dfs(index + 1, seq[index], right) + move(left, seq[index]))
    if left != seq[index]:
        temp = min(temp, dfs(index + 1, left, seq[index]) + move(right, seq[index]))
    cache[index][left][right] = temp
    return cache[index][left][right]


def main():
    global n, seq, cache
    seq = list(map(int, input().split()))
    seq.pop()
    n = len(seq)
    cache = [[[-1] * 5 for _ in range(5)] for _ in range(n)]
    print(dfs(0, 0, 0))


if __name__ == "__main__":
    main()
