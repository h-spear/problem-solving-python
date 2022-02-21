# https://programmers.co.kr/learn/courses/30/lessons/49994

dx = {"L": 0, "R": 0, "U": -1, "D": 1}
dy = {"L": -1, "R": 1, "U": 0, "D": 0}


def solution(dirs):
    x, y = 0, 0

    visited = set()
    for dir in dirs:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if abs(nx) > 5 or abs(ny) > 5:
            continue
        visited.add((x, y, nx, ny))
        visited.add((nx, ny, x, y))
        x, y = nx, ny

    return len(visited) // 2
