# https://www.acmicpc.net/problem/2042
# https://velog.io/@corone_hi/%EA%B5%AC%EA%B0%84-%ED%8A%B8%EB%A6%AC-Segment-Tree-Python

import sys

input = lambda: sys.stdin.readline().rstrip()


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(
            node * 2 + 1, (start + end) // 2 + 1, end
        )
        return tree[node]


def sub_sum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return sub_sum(node * 2, start, (start + end) // 2, left, right) + sub_sum(
        node * 2 + 1, (start + end) // 2 + 1, end, left, right
    )


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)


n, m, k = map(int, input().rstrip().split())

l = []
tree = [0] * 3000000

for _ in range(n):
    l.append(int(input()))

init(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        b = b - 1
        diff = c - l[b]
        l[b] = c
        update(1, 0, n - 1, b, diff)
    elif a == 2:
        print(sub_sum(1, 0, n - 1, b - 1, c - 1))
