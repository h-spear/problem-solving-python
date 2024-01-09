# https://www.acmicpc.net/problem/3109

import sys

input = lambda: sys.stdin.readline().rstrip()

R = -1
C = -1
is_wall = None
visited = None


def dfs(x, y):
    if y == C - 1:
        return True

    visited[x][y] = True
    for nx in [x - 1, x, x + 1]:
        if nx < 0 or nx >= R:
            continue
        if not is_wall[nx][y + 1] and not visited[nx][y + 1]:
            if dfs(nx, y + 1):
                return True

    return False


def main():
    global R, C, is_wall, visited
    R, C = map(int, input().split())
    visited = [[False] * C for _ in range(R)]
    is_wall = [[True if x == "x" else False for x in input()] for _ in range(R)]
    print(sum([1 if dfs(x, 0) else 0 for x in range(R)]))


if __name__ == "__main__":
    main()
