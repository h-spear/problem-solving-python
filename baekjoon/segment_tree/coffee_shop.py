# https://www.acmicpc.net/problem/1275

import sys


def init(node, start, end):
    if start == end:
        tree[node] = li[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(node * 2, start, mid) + init(node * 2 + 1, mid + 1, end)
    return tree[node]


def query(node, start, end, left, right):
    if end < left or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


def update(node, start, end, index, val):
    if end < index or index < start:
        return

    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


input = lambda: sys.stdin.readline().rstrip()

n, q = map(int, input().split())
li = list(map(int, input().split()))
tree = [0] * (n * 4)
init(1, 0, n - 1)
for _ in range(q):
    *t, a, b = map(int, input().split())
    x, y = min(t), max(t)
    print(query(1, 0, n - 1, x - 1, y - 1))
    update(1, 0, n - 1, a - 1, b)
