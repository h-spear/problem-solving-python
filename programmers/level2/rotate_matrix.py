# https://programmers.co.kr/learn/courses/30/lessons/77485


def rotate_matrix(mat, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    topleft = mat[x1][y1]
    topright = mat[x1][y2]
    bottomleft = mat[x2][y1]
    bottomright = mat[x2][y2]
    minimum = min(topleft, topright, bottomleft, bottomright)

    for j in range(y2, y1, -1):
        mat[x1][j] = mat[x1][j - 1]
        minimum = min(minimum, mat[x1][j])
    for i in range(x2, x1, -1):
        mat[i][y2] = mat[i - 1][y2]
        minimum = min(minimum, mat[i][y2])
    for j in range(y1 + 1, y2):
        mat[x2][j - 1] = mat[x2][j]
        minimum = min(minimum, mat[x2][j - 1])
    for i in range(x1 + 1, x2):
        mat[i - 1][y1] = mat[i][y1]
        minimum = min(minimum, mat[i - 1][y1])

    mat[x1][y1 + 1] = topleft
    mat[x1 + 1][y2] = topright
    mat[x2][y2 - 1] = bottomright
    mat[x2 - 1][y1] = bottomleft

    return minimum


def solution(rows, columns, queries):
    answer = []
    mat = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for j in range(columns):
            mat[i][j] = cnt
            cnt += 1

    for query in queries:
        answer.append(rotate_matrix(mat, *query))
    return answer
