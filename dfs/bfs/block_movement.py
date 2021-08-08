# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

# up right down left
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
extended_board = None


def movement(pos):
    global extended_board
    cases = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    for i in range(4):
        next_pos1_x, next_pos1_y, next_pos2_x, next_pos2_y = (
            pos1_x + dx[i],
            pos1_y + dy[i],
            pos2_x + dx[i],
            pos2_y + dy[i],
        )

        if (
            extended_board[next_pos1_x][next_pos1_y] == 0
            and extended_board[next_pos2_x][next_pos2_y] == 0
        ):
            cases.append({(next_pos1_x, next_pos1_y), (next_pos2_x, next_pos2_y)})

    # 로봇이 가로로 놓여있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if (
                extended_board[pos1_x + i][pos1_y] == 0
                and extended_board[pos2_x + i][pos2_y] == 0
            ):
                cases.append({(pos1_x + i, pos1_y), (pos1_x, pos1_y)})
                cases.append({(pos2_x + i, pos2_y), (pos2_x, pos2_y)})

    # 로봇이 세로로 놓여있는 경우
    if pos1_y == pos2_y:
        for i in [-1, 1]:
            if (
                extended_board[pos1_x][pos1_y + i] == 0
                and extended_board[pos2_x][pos2_y + i] == 0
            ):
                cases.append({(pos1_x, pos1_y + i), (pos1_x, pos1_y)})
                cases.append({(pos2_x, pos2_y + i), (pos2_x, pos2_y)})

    return cases


def solution(board):
    global extended_board
    n = len(board)

    extended_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            extended_board[i][j] = board[i - 1][j - 1]

    visited = []

    start = {(1, 1), (1, 2)}
    q = deque([(start, 0)])
    visited.append(start)

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost

        for case in movement(pos):
            if case not in visited:
                q.append((case, cost + 1))
                visited.append(case)
    return 0


board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
]
print(solution(board))
