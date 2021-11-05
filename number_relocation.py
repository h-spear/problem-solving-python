# https://www.acmicpc.net/problem/16943

from itertools import permutations

a, b = input().split()
a = list(a)
b = int(b)

answer = -1
for candidate in permutations(a, len(a)):
    if candidate[0] == "0":
        continue
    now = int("".join(candidate))
    if now < b:
        answer = max(answer, now)

print(answer)
