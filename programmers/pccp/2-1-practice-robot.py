# https://school.programmers.co.kr/learn/courses/15009/lessons/121687


def solution(command):
    # 0:UP, 1: RIGHT, 2: DOWN, 3:LEFT
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    x, y = 0, 0

    for c in command:
        if c == "R":
            direction = (direction + 1) % 4
        elif c == "L":
            direction = (direction - 1) % 4
        elif c == "G":
            x += dx[direction]
            y += dy[direction]
        elif c == "B":
            x -= dx[direction]
            y -= dy[direction]

    return [x, y]
