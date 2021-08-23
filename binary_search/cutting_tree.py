# https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))


def calc(h):
    sum = 0
    for x in data:
        if x > h:
            sum += x - h
    return sum


def solution(left, right):
    if left > right:
        return right

    mid = (left + right) // 2

    comp = calc(mid)
    if comp < m:
        return solution(left, mid - 1)
    elif comp >= m:
        return solution(mid + 1, right)


print(solution(1, max(data)))
