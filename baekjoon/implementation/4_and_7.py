# https://www.acmicpc.net/problem/2877

from typing import *

k: int = int(input())

i: int = 0
length: int = 0
idx: int
c: int

while i < k:
    length += 1
    i += 2 ** length

i -= 2 ** length
idx = k - i
c = 2 ** length

answer: List[str] = []

for l in range(length, 0, -1):
    if idx > 2 ** (l - 1):
        answer.append("7")
        idx -= 2 ** (l - 1)
    else:
        answer.append("4")

print("".join(answer))
