# https://www.acmicpc.net/problem/20055

from collections import deque

n, k = map(int, input().split())
A = list(map(int, input().split()))
belt = deque()
for d in A:
    belt.append([d, False])


def unload_robot():
    global belt
    if belt[n - 1][1] == True:
        belt[n - 1][1] = False


def belt_rotate():
    global belt
    belt.appendleft(belt.pop())
    unload_robot()


def robot_move():
    global belt
    for i in range(2 * n - 1, -1, -1):
        forward = (i + 1) % (2 * n)
        if belt[i][1] == True and (belt[forward][0] >= 1 and belt[forward][1] == False):
            belt[forward][0] -= 1
            belt[forward][1], belt[i][1] = belt[i][1], belt[forward][1]
    unload_robot()


def put_robot():
    global belt
    if belt[0][0] >= 1:
        belt[0][1] = True
        belt[0][0] -= 1


def check_state():
    cnt = 0
    for state, _ in belt:
        if state == 0:
            cnt += 1
    return cnt >= k


def simulate():
    cnt = 1
    while 1:
        belt_rotate()
        robot_move()
        put_robot()
        if check_state():
            return cnt
        cnt += 1


print(simulate())
