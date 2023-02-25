# https://www.acmicpc.net/problem/2268

import sys

input = lambda: sys.stdin.readline().rstrip()


def modify(node, start, end, index, val):
    if end < index or index < start:
        return
    if index == start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    modify(node * 2, start, mid, index, val)
    modify(node * 2 + 1, mid + 1, end, index, val)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def query(node, start, end, left, right):
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return query(node * 2, start, mid, left, right) + query(
        node * 2 + 1, mid + 1, end, left, right
    )


n, m = map(int, input().split())
tree = [0] * 4000040
A = [0] * 1000010
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        a, b = min(a, b), max(a, b)
        print(query(1, 0, n - 1, a - 1, b - 1))
    else:
        modify(1, 0, n - 1, a - 1, b)
