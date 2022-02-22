# https://programmers.co.kr/learn/courses/30/lessons/12905
# dp


def solution(board):
    answer = 0
    r = len(board)
    c = len(board[0])

    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 0:
                continue
            board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    answer = 0
    for i in range(r):
        for j in range(c):
            answer = max(answer, board[i][j])

    return answer ** 2
