# https://www.acmicpc.net/problem/2414
# *** 테이프를 붙일 때에는 구멍이 뚫려 있지 않은 부분을 막아서는 안 된다

def dfs(num1):
    if visit[num1]:
        return False
    visit[num1] = True

    for num2 in graph[num1]:
        if not match[num2] or dfs(match[num2]):
            match[num2] = num1
            return True

    return False


MAX_NUMBER = 2500
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
graph = [[] for _ in range(MAX_NUMBER + 1)]
visit = None
match = [0] * (MAX_NUMBER + 1)
board_1 = [[0] * m for _ in range(n)]
board_2 = [[0] * m for _ in range(n)]
answer = 0

# numbering
number = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == "*":
            board_1[i][j] = number
        else:
            number += 1
    number += 1

number = 1
for j in range(m):
    for i in range(n):
        if board[i][j] == "*":
            board_2[i][j] = number
        else:
            number += 1
    number += 1

# construct graph
for i in range(n):
    for j in range(m):
        if board[i][j] == ".":
            continue
        graph[board_1[i][j]].append(board_2[i][j])

# bipartite matching
for i in range(MAX_NUMBER):
    if graph[i]:
        visit = [False] * (MAX_NUMBER + 1)
        if dfs(i):
            answer += 1

print(answer)
