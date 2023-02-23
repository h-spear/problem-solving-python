# https://school.programmers.co.kr/learn/courses/30/lessons/160585

gBoard = None
gTarget = None
answer = 0
nextTurn = {"O": "X", "X": "O"}


def dfs(turn, depth):
    global answer

    if answer == 1:
        return
    if check_target():
        answer = 1
        return
    if is_game_end():
        return

    for i in range(3):
        for j in range(3):
            if gBoard[i][j] != ".":
                continue
            gBoard[i][j] = turn
            dfs(nextTurn[turn], depth + 1)
            gBoard[i][j] = "."


def check_target():
    for i in range(3):
        for j in range(3):
            if gBoard[i][j] != gTarget[i][j]:
                return False
    return True


def is_game_end():
    # 가로 체크
    for i in range(3):
        oCnt = 0
        xCnt = 0
        for j in range(3):
            if gBoard[i][j] == "O":
                oCnt += 1
            elif gBoard[i][j] == "X":
                xCnt += 1
        if oCnt == 3 or xCnt == 3:
            return True

    # 세로 체크
    for j in range(3):
        oCnt = 0
        xCnt = 0
        for i in range(3):
            if gBoard[i][j] == "O":
                oCnt += 1
            elif gBoard[i][j] == "X":
                xCnt += 1
        if oCnt == 3 or xCnt == 3:
            return True

    # 대각선 체크
    oCnt = 0
    xCnt = 0
    for i in range(3):
        if gBoard[i][i] == "O":
            oCnt += 1
        elif gBoard[i][i] == "X":
            xCnt += 1
    if oCnt == 3 or xCnt == 3:
        return True

    oCnt = 0
    xCnt = 0
    for i in range(3):
        if gBoard[i][2 - i] == "O":
            oCnt += 1
        elif gBoard[i][2 - i] == "X":
            xCnt += 1
    if oCnt == 3 or xCnt == 3:
        return True

    return False


def solution(board):
    global answer, gBoard, gTarget
    gBoard = [["."] * 3 for _ in range(3)]
    gTarget = [list(line) for line in board]
    dfs("O", 0)
    return answer
