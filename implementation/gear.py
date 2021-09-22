# https://www.acmicpc.net/problem/14891

from collections import deque
from copy import deepcopy

gear = [0]
gear_copy = None
for _ in range(4):
    gear.append(deque(map(int, list(input()))))


def clockwise(num):
    gear[num].appendleft(gear[num].pop())


def counterclockwise(num):
    gear[num].append(gear[num].popleft())


rotated = [False] * 5


def rotate(num, dir):
    if dir == 1:
        clockwise(num)
    else:
        counterclockwise(num)
    rotated[num] = True

    if num + 1 <= 4:
        if rotated[num + 1] == False and gear_copy[num][2] != gear_copy[num + 1][6]:
            rotate(num + 1, -dir)
    if num - 1 >= 1:
        if rotated[num - 1] == False and gear_copy[num][6] != gear_copy[num - 1][2]:
            rotate(num - 1, -dir)


def score():
    result = 0
    result += 0 if gear[1][0] == 0 else 1
    result += 0 if gear[2][0] == 0 else 2
    result += 0 if gear[3][0] == 0 else 4
    result += 0 if gear[4][0] == 0 else 8
    return result


def rotatedClear():
    for i in range(5):
        rotated[i] = False


for _ in range(int(input())):
    number, direction = map(int, input().split())
    rotatedClear()
    gear_copy = deepcopy(gear)
    rotate(number, direction)

print(score())
