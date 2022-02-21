# https://www.acmicpc.net/problem/2470

from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
A.sort()
answer = 3000000000
result = None
for idx, x in enumerate(A):
    i = bisect_left(A, -x)
    for j in [i - 1, i, i + 1]:
        if j >= n:
            continue
        if j == idx:
            continue
        if abs(answer) > abs(x + A[j]):
            answer = x + A[j]
            result = [x, A[j]]

result.sort()
print(result[0], result[1])
