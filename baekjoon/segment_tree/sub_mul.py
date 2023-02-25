# https://www.acmicpc.net/problem/11505

import sys

input = lambda: sys.stdin.readline().rstrip()


def init(node, start, end):
    if start == end:
        tree[node] = A[start]
    else:
        mid = (start + end) // 2
        tree[node] = (init(node * 2, start, mid) * init(node * 2 + 1, mid + 1, end)) % p
    return tree[node]


def query(node, start, end, left, right):
    if end < left or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (
        query(node * 2, start, mid, left, right)
        * query(node * 2 + 1, mid + 1, end, left, right)
    ) % p


def update(node, start, end, index, value):
    if index < start or end < index:
        return

    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % p


p = 1000000007
n, m, k = map(int, input().split())
tree = [0] * (n * 4)
A = []
for _ in range(n):
    A.append(int(input()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        update(1, 0, n - 1, b - 1, c)
    else:
        print(query(1, 0, n - 1, b - 1, c - 1))
