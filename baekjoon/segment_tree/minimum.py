# https://www.acmicpc.net/problem/10868

import sys


def init(node, start, end):
    if start == end:
        tree[node] = A[start]
        return tree[node]
    else:
        tree[node] = min(
            init(node * 2, start, (start + end) // 2),
            init(node * 2 + 1, (start + end) // 2 + 1, end),
        )
        return tree[node]


def query(node, start, end, left, right):
    if left > end or right < start:
        return INF

    if left <= start and end <= right:
        return tree[node]

    return min(
        query(node * 2, start, (start + end) // 2, left, right),
        query(node * 2 + 1, (start + end) // 2 + 1, end, left, right),
    )


input = lambda: sys.stdin.readline().rstrip()
INF = 1000000010
n, m = map(int, input().split())
tree = [0] * (n * 4)
A = []
for _ in range(n):
    A.append(int(input()))

init(1, 0, len(A) - 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(query(1, 0, len(A) - 1, a - 1, b - 1))
