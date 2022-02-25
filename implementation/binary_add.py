# https://www.acmicpc.net/problem/2729

from collections import deque


def add(a, b):
    la = len(a)
    lb = len(b)

    a.appendleft(0)
    b.appendleft(0)
    if la < lb:
        for _ in range(lb - la):
            a.appendleft(0)
    else:
        for _ in range(la - lb):
            b.appendleft(0)

    l = len(a)
    result = deque([0] * l)
    for i in range(l - 1, 0, -1):
        added = a[i] + b[i] + result[i]
        result[i] = added % 2
        result[i - 1] = added // 2

    while result and result[0] == 0:
        result.popleft()

    if not result:
        print(0)
        return

    for x in result:
        print(x, end="")
    print()


for tc in range(int(input())):
    a, b = input().split()
    a = deque(list(map(int, a)))
    b = deque(list(map(int, b)))
    add(a, b)
