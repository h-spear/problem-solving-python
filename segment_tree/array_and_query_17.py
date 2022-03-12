# https://www.acmicpc.net/problem/14438

import sys


def init(node, start, end):
    if start == end:
        tree[node] = A[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init(node * 2, start, mid), init(node * 2 + 1, mid + 1, end))
    return tree[node]


def query(node, start, end, left, right):
    if end < left or right < start:
        return int(1e9)

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    return min(
        query(node * 2, start, mid, left, right),
        query(node * 2 + 1, mid + 1, end, left, right),
    )


def update(node, start, end, index, value):
    # 리프노드부터 업데이트
    if index < start or index > end:
        return

    if start == end:
        tree[node] = value  # leaf node update
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


input = lambda: sys.stdin.readline().rstrip()
n = int(input())
A = list(map(int, input().split()))
m = int(input())
tree = [0] * (n * 4)
init(1, 0, n - 1)
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 1:
        update(1, 0, n - 1, a - 1, b)
        A[a - 1] = b
    else:
        print(query(1, 0, n - 1, a - 1, b - 1))
