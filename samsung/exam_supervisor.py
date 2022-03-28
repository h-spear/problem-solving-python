# https://www.acmicpc.net/problem/13458

import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = len(a)

for x in a:
    if x - b <= 0:
        continue
    answer += math.ceil((x - b) / c)

print(answer)
