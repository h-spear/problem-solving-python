# https://www.acmicpc.net/problem/3066

from bisect import bisect_left


def lis_length(arr):
    length = 0
    q = []
    for x in arr:
        if not q:
            length += 1
            q.append(x)
            continue

        if q[-1] < x:
            length += 1
            q.append(x)
        else:
            index = bisect_left(q, x)
            q[index] = x
    return length


for tc in range(int(input())):
    n = int(input())
    k = []
    for i in range(n):
        k.append(int(input()))

    print(lis_length(k))
