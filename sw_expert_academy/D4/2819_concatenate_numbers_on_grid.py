# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV7I5fgqEogDFAXB&categoryId=AV7I5fgqEogDFAXB&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())


def dfs(graph, x, y, numstr, s, depth):
    if depth == 7:
        s.add(numstr)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4:
            continue
        dfs(graph, nx, ny, numstr + str(graph[nx][ny]), s, depth + 1)


def handler(graph, s):
    for i in range(4):
        for j in range(4):
            dfs(graph, i, j, "", s, 0)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    s = set()
    graph = [list(map(int, input().split())) for _ in range(4)]
    handler(graph, s)
    print(f"#{test_case} {len(s)}")
    # ///////////////////////////////////////////////////////////////////////////////////
