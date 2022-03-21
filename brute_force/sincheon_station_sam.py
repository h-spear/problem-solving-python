# https://www.acmicpc.net/problem/14650

from itertools import product

n = int(input())
answer = 0
for x in product([0, 1, 2], repeat=n):
    num = int("".join(list(map(str, x))))
    if num == 0:
        continue
    if len(str(num)) != n:
        continue
    if num % 3 == 0:
        answer += 1

print(answer)
