# https://www.acmicpc.net/problem/20300

from collections import deque

n = int(input())
t = list(map(int, input().split()))
t.sort()
t = deque(t)
answer = 0
if n & 1:
    answer = t.pop()

while len(t) >= 2:
    answer = max(t.pop() + t.popleft(), answer)

print(answer)
