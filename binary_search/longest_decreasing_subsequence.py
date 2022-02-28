# https://www.acmicpc.net/problem/11722

from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

q = []
answer = 0
for x in array:
    if not q or q[-1] < -x:
        answer += 1
        q.append(-x)
    else:
        idx = bisect_left(q, -x)
        q[idx] = -x

print(answer)
