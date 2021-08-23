# https://www.acmicpc.net/problem/1654

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
data = []
for _ in range(k):
    data.append(int(input()))


def cutting(len):
    cnt = 0
    for x in data:
        cnt += x // len
    return cnt


def binary_search(left, right):
    if left > right:
        return right

    mid = (left + right) // 2
    cnt = cutting(mid)
    if cnt >= n:
        return binary_search(mid + 1, right)
    elif cnt < n:
        return binary_search(left, mid - 1)


print(binary_search(1, max(data)))
