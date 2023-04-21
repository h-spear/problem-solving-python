# https://www.acmicpc.net/problem/17128

from typing import *


n: int
q: int
i: int

n, q = map(int, input().split())

A: List[int] = list(map(int, input().split()))
A.extend(A[0:4].copy())
mischief: List[int] = list(map(int, input().split()))

arr: List[int] = []

arr.append(A[0] * A[1] * A[2] * A[3])
for i in range(1, n):
    arr.append((arr[i - 1] * A[i + 3]) // A[i - 1])

s: int = sum(arr)
cow: int

for cow in mischief:
    cow -= 1

    for _ in range(4):
        s -= 2 * arr[cow]
        arr[cow] *= -1
        cow = (cow - 1) % len(arr)

    print(s)
