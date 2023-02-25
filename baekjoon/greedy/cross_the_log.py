# https://www.acmicpc.net/problem/11497

from collections import deque

for tc in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a = deque()
    a.append(l.pop())
    while l:
        one = l.pop()
        a.append(one)

        if not l:
            break

        two = l.pop()
        a.appendleft(two)

    answer = 0
    for i in range(-1, n - 1):
        answer = max(answer, abs(a[i] - a[i + 1]))

    print(answer)
