# https://www.acmicpc.net/problem/12015
# https://www.acmicpc.net/problem/12738
# https://www.acmicpc.net/problem/14003
# 최장 증가 부분 수열, Longest Increasing Subsequence
# O(nlogn)
from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
q = []
temp = []

for x in array:
    if not q or q[-1] < x:
        q.append(x)
        temp.append((len(q) - 1, x))
    else:
        index = bisect_left(q, x)
        q[index] = x
        temp.append((index, x))

answer = []
now = len(q) - 1
print(len(q))
for i in range(len(temp) - 1, -1, -1):
    if temp[i][0] == now:
        answer.append(temp[i][1])
        now -= 1

for x in sorted(answer):
    print(x, end=" ")
