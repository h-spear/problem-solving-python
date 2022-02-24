# https://www.acmicpc.net/problem/2615


def check_pos(board, x, y):
    found = True
    for nx in [x - 2, x - 1, x + 1, x + 2]:
        if nx < 0 or nx >= 19 or board[nx][y] != board[x][y]:
            found = False
            break
    if found:
        if x - 3 >= 0 and board[x - 3][y] == board[x][y]:
            pass
        elif x + 3 < 19 and board[x + 3][y] == board[x][y]:
            pass
        else:
            return (x - 2, y, board[x][y])

    found = True
    for ny in [y - 2, y - 1, y + 1, y + 2]:
        if ny < 0 or ny >= 19 or board[x][ny] != board[x][y]:
            found = False
            break
    if found:
        if y - 3 >= 0 and board[x][y - 3] == board[x][y]:
            pass
        elif y + 3 < 19 and board[x][y + 3] == board[x][y]:
            pass
        else:
            return (x, y - 2, board[x][y])

    found = True
    for i in [-2, -1, 1, 2]:
        nx = x + i
        ny = y + i
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19 or board[nx][ny] != board[x][y]:
            found = False
            break
    if found:
        if x - 3 >= 0 and y - 3 >= 0 and board[x - 3][y - 3] == board[x][y]:
            pass
        elif x + 3 < 19 and y + 3 < 19 and board[x + 3][y + 3] == board[x][y]:
            pass
        else:
            return (x - 2, y - 2, board[x][y])

    found = True
    for i in [-2, -1, 1, 2]:
        nx = x + i
        ny = y - i
        if nx < 0 or nx >= 19 or ny < 0 or ny >= 19 or board[nx][ny] != board[x][y]:
            found = False
            break
    if found:
        if x - 3 >= 0 and y + 3 < 19 and board[x - 3][y + 3] == board[x][y]:
            pass
        elif x + 3 < 19 and y - 3 >= 0 and board[x + 3][y - 3] == board[x][y]:
            pass
        else:
            return (x + 2, y - 2, board[x][y])

    return None


def simulate(board):
    for i in range(19):
        for j in range(19):
            if board[i][j] == 0:
                continue

            res = check_pos(board, i, j)
            if res != None:
                print(res[2])
                print(res[0] + 1, res[1] + 1)
                return
    print(0)


board = [list(map(int, input().split())) for _ in range(19)]
simulate(board)
