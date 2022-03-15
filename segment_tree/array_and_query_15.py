# https://www.acmicpc.net/problem/14427

import sys

input = lambda: sys.stdin.readline().rstrip()


def init(node, start, end):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        L = init(node * 2, start, mid)
        R = init(node * 2 + 1, mid + 1, end)
        if A[L] == A[R]:
            tree[node] = min(L, R)
        elif A[L] < A[R]:
            tree[node] = L
        else:
            tree[node] = R
    return tree[node]


def query(node, start, end, left, right):
    if end < left or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    L = query(node * 2, start, mid, left, right)
    R = query(node * 2 + 1, mid + 1, end, left, right)
    if L == -1:
        return R
    elif R == -1:
        return L
    elif A[L] == A[R]:
        return min(L, R)
    elif A[L] < A[R]:
        return L
    else:
        return R


def update(node, start, end, index, val):
    if index < start or index > end:
        return

    if start == end:
        A[index] = val
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, val)
    update(node * 2 + 1, mid + 1, end, index, val)

    if A[tree[node * 2]] <= A[tree[node * 2 + 1]]:
        tree[node] = tree[node * 2]
    else:
        tree[node] = tree[node * 2 + 1]


n = int(input())
A = list(map(int, input().split()))
m = int(input())
tree = [0] * (n * 4)
init(1, 0, n - 1)
for _ in range(m):
    c, *x = map(int, input().split())
    if c == 1:
        i, v = x
        update(1, 0, n - 1, i - 1, v)
    else:
        print(query(1, 0, n - 1, 0, n - 1) + 1)
