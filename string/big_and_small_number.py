# https://www.acmicpc.net/problem/2992

from itertools import permutations

INF = 1234567
x = input()
lx = len(x)
answer = INF
for c in permutations(x, lx):
    num = int("".join(c))
    if num > int(x) and num < answer:
        answer = num

if answer == INF:
    print(0)
else:
    print(answer)
