# https://www.acmicpc.net/problem/6549

import sys

sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()


def init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    else:
        mid = (start + end) // 2
        left_child = init(node * 2, start, mid)
        right_child = init(node * 2 + 1, mid + 1, end)

        if A[left_child] < A[right_child]:
            tree[node] = left_child
        else:
            tree[node] = right_child
        return tree[node]


def query(node, start, end, left, right):
    if end < left or right < start:
        return -1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_child = query(node * 2, start, mid, left, right)
    right_child = query(node * 2 + 1, mid + 1, end, left, right)

    if left_child == -1:
        return right_child
    elif right_child == -1:
        return left_child
    else:
        if A[left_child] < A[right_child]:
            return left_child
        else:
            return right_child


def solve(left, right):
    index = query(1, 0, n - 1, left, right)

    if left == right:
        return A[index]

    v1 = A[index] * (right - left + 1)
    v2, v3 = 0, 0

    if index - 1 >= left:
        v2 = solve(left, index - 1)
    if index + 1 <= right:
        v3 = solve(index + 1, right)

    return max(v1, v2, v3)


while 1:
    n, *A = list(map(int, input().split()))
    if n == 0:
        break
    tree = [0] * (n * 4)
    init(1, 0, n - 1)
    print(solve(0, n - 1))
