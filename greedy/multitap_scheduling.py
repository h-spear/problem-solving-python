# https://www.acmicpc.net/problem/1700

import sys

input = lambda: sys.stdin.readline().rstrip()
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = set()
answer = 0

for i, x in enumerate(a):
    if x in s:
        continue

    if len(s) < n:
        s.add(x)
    else:
        removed = 0
        idx = -1
        for r in s:
            try:
                temp = a[i + 1 :].index(r)
            except:
                removed = r
                break

            if temp > idx:
                idx = temp
                removed = r

        answer += 1
        if removed:
            s.remove(removed)
            s.add(x)

print(answer)
