# https://school.programmers.co.kr/learn/courses/30/lessons/120861


def solution(keyinput, board):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    direction = {"up": 0, "down": 1, "left": 2, "right": 3}
    x, y = 0, 0
    w, h = board[0] // 2, board[1] // 2
    for key in keyinput:
        i = direction[key]
        nx = x + dx[i]
        ny = y + dy[i]
        if -w <= nx <= w and -h <= ny <= h:
            x, y = nx, ny

    return [x, y]
