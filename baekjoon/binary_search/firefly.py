# https://www.acmicpc.net/problem/3020

from bisect import bisect_left
from collections import defaultdict

n, h = map(int, input().split())
below = []
above = []
for i in range(n):
    if i & 1:
        above.append(h - int(input()))
    else:
        below.append(int(input()))

below.sort()
above.sort()

la = len(above)
lb = len(below)

hash = defaultdict(int)
minima = 1234567
for height in range(1, h + 1):
    ubb = bisect_left(below, height)
    lba = bisect_left(above, height)

    cnt = lb - ubb + lba
    hash[cnt] += 1
    minima = min(minima, cnt)

print(minima, hash[minima])
