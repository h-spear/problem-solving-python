# https://www.acmicpc.net/problem/1725
import sys

sys.setrecursionlimit(10 ** 5)


def init(node, start, end):
    if start == end:
        tree[node] = start
    else:
        mid = (start + end) // 2
        L = init(node * 2, start, mid)
        R = init(node * 2 + 1, mid + 1, end)

        if A[L] < A[R]:
            tree[node] = L
        else:
            tree[node] = R

    return tree[node]


def get_min_index(node, start, end, left, right):
    if end < left or start > right:
        return -1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    L = get_min_index(node * 2, start, mid, left, right)
    R = get_min_index(node * 2 + 1, mid + 1, end, left, right)

    if L == -1:
        return R
    if R == -1:
        return L

    if A[L] < A[R]:
        return L
    else:
        return R


def solve(left, right):
    if left == right:
        return A[left]

    index = get_min_index(1, 0, n - 1, left, right)
    v1 = A[index] * (right - left + 1)
    v2, v3 = 0, 0

    if index - 1 >= left:
        v2 = solve(left, index - 1)
    if index + 1 <= right:
        v3 = solve(index + 1, right)

    return max(v1, v2, v3)


n = int(input())
A = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)
init(1, 0, n - 1)
print(solve(0, n - 1))
