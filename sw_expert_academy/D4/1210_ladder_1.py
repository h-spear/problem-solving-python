# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14ABYKADACFAYh&categoryId=AV14ABYKADACFAYh&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

from collections import deque

T = 10
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    ladder = []
    tc = int(input())
    n = 100
    for _ in range(n):
        ladder.append(list(map(int, input().split())))

    x, y = n - 1, ladder[-1].index(2)
    visited = set()
    dx = [0, 0, -1]
    dy = [1, -1, 0]
    while 1:
        if x == 0:
            break
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or ny >= n:
                continue
            if not ladder[nx][ny]:
                continue
            if (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            x = nx
            y = ny
            break

    print(f"#{tc} {y}")

    # ///////////////////////////////////////////////////////////////////////////////////
