# https://school.programmers.co.kr/learn/courses/30/lessons/72415
# https://www.youtube.com/watch?v=Q4bTSdi1psw

from collections import deque, defaultdict

INF = float("inf")
g_board = []
all_card = defaultdict(list)
all_removed = 1
min_cnt = INF
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(removed, src, dst):
    visited = [[0] * 4 for _ in range(4)]
    q = deque()
    q.append(src)
    while q:
        x, y, cnt = q.popleft()
        if x == dst[0] and y == dst[1]:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

            for j in range(2):
                if (removed & 1 << g_board[nx][ny]) == 0:
                    break
                if nx + dx[i] < 0 or nx + dx[i] > 3 or ny + dy[i] < 0 or ny + dy[i] > 3:
                    break
                nx += dx[i]
                ny += dy[i]

            if not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny, cnt + 1))

    return INF


def permutate(cnt, removed, src):
    global min_cnt

    if cnt >= min_cnt:
        return

    if removed == all_removed:
        min_cnt = min(min_cnt, cnt)
        return

    for num, card in all_card.items():
        if removed & 1 << num:
            continue

        # src: 시작 위치
        one = bfs(removed, src, card[0]) + bfs(removed, card[0], card[1]) + 2
        two = bfs(removed, src, card[1]) + bfs(removed, card[1], card[0]) + 2

        permutate(cnt + one, removed | 1 << num, card[1])
        permutate(cnt + two, removed | 1 << num, card[0])


def solution(board, r, c):
    global g_board, all_card, all_removed
    g_board = board

    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num:
                all_removed |= 1 << num
                all_card[num].append((i, j, 0))

    permutate(0, 1, (r, c, 0))
    return min_cnt
