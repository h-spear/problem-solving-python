# https://www.acmicpc.net/problem/2357

import sys


def init(tree, node, start, end, calc_max=True):
    if start == end:
        tree[node] = A[start]
    else:
        mid = (start + end) // 2
        if calc_max:
            tree[node] = max(
                init(tree, node * 2, start, mid), init(tree, node * 2 + 1, mid + 1, end)
            )
        else:
            tree[node] = min(
                init(tree, node * 2, start, mid, False),
                init(tree, node * 2 + 1, mid + 1, end, False),
            )
    return tree[node]


def query(tree, node, start, end, left, right, calc_max=True):
    if left > end or start > right:
        return INF * (-1 if calc_max else 1)

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    if calc_max:
        return max(
            query(tree, node * 2, start, mid, left, right),
            query(tree, node * 2 + 1, mid + 1, end, left, right),
        )
    else:
        return min(
            query(tree, node * 2, start, mid, left, right, False),
            query(tree, node * 2 + 1, mid + 1, end, left, right, False),
        )


input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
A = []
max_tree = [0] * (n * 4)
min_tree = [0] * (n * 4)
INF = 1000000000
for _ in range(n):
    A.append(int(input()))

init(max_tree, 1, 0, n - 1)
init(min_tree, 1, 0, n - 1, False)

for _ in range(m):
    a, b = map(int, input().split())
    print(
        query(min_tree, 1, 0, n - 1, a - 1, b - 1, False),
        query(max_tree, 1, 0, n - 1, a - 1, b - 1),
    )
