# https://www.acmicpc.net/problem/15662

import sys
from collections import deque

input = lambda:sys.stdin.readline().rstrip()
t = int(input())
gear = []
for _ in range(t):
    gear.append(deque(list(map(int, list(input())))))

k = int(input())
command = []
for _ in range(k):
    num, dir = map(int, input().split())
    command.append((num - 1, dir))


def func(num, dir, visited):
    visited[num] = dir
    curr = gear[num]
    left = gear[num - 1] if num - 1 >= 0 else None
    right = gear[num + 1] if num + 1 < t else None

    if left and not visited[num - 1] != 0 and left[2] != curr[6]:
        func(num - 1, -dir, visited)

    if right and not visited[num + 1] != 0 and right[6] != curr[2]:
        func(num + 1, -dir, visited)


def rotate(num, dir):
    visited = [0] * t
    func(num, dir, visited)
    for num, dir in enumerate(visited):
        if dir == 1:
            gear[num].appendleft(gear[num].pop())
        elif dir == -1:
            gear[num].append(gear[num].popleft())


for num, dir in command:
    rotate(num, dir)

answer = 0
for num in range(t):
    answer += gear[num][0]

print(answer)
