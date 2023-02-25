# https://www.acmicpc.net/problem/16975

import sys

input = lambda: sys.stdin.readline().rstrip()


def initialize(node, start, end):
    if start == end:
        tree[node] = A[start]
    else:
        mid = (start + end) // 2
        initialize(node * 2, start, mid)
        initialize(node * 2 + 1, mid + 1, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def propagate(node, start, end):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]

        if start != end:
            lazy[node * 2] += lazy[node]
            lazy[node * 2 + 1] += lazy[node]

        lazy[node] = 0


def query(node, start, end, left, right):
    propagate(node, start, end)

    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


def update(node, start, end, left, right, diff):
    propagate(node, start, end)

    if end < left or right < start:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * diff

        if start != end:
            lazy[node * 2] += diff
            lazy[node * 2 + 1] += diff
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, left, right, diff)
    update(node * 2 + 1, mid + 1, end, left, right, diff)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


n = int(input())
A = list(map(int, input().split()))
tree = [0] * (n * 4)
lazy = [0] * (n * 4)
initialize(1, 0, n - 1)

m = int(input())
for _ in range(m):
    c, *x = map(int, input().split())
    if c == 1:
        i, j, k = x
        update(1, 0, n - 1, i - 1, j - 1, k)
    else:
        x = x[0]
        print(query(1, 0, n - 1, x - 1, x - 1))
