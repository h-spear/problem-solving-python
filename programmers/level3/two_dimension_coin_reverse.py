# https://school.programmers.co.kr/learn/courses/30/lessons/131703

INF = 12345678
gBeginning = None
gTarget = None
m, n = 0, 0
answer = INF


def reverse(idx):
    if idx >= m:
        j = idx - m
        for i in range(m):
            gBeginning[i][j] = 1 - gBeginning[i][j]
    else:
        i = idx
        for j in range(n):
            gBeginning[i][j] = 1 - gBeginning[i][j]


def check():
    for i in range(m):
        for j in range(n):
            if gBeginning[i][j] != gTarget[i][j]:
                return False
    return True


def dfs(idx, depth=0):
    global answer
    if check():
        answer = min(answer, depth)
        return

    for i in range(idx + 1, m + n):
        reverse(i)
        dfs(i, depth + 1)
        reverse(i)


def solution(beginning, target):
    global gBeginning, gTarget, answer, m, n
    gBeginning = beginning
    gTarget = target
    m, n = len(beginning), len(beginning[0])
    dfs(-1)
    return -1 if answer == INF else answer
