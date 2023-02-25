# https://www.acmicpc.net/problem/15684


def run(ladder, idx):
    for height in range(h):
        if idx > 0 and ladder[height][idx - 1]:
            idx -= 1
        elif idx < n - 1 and ladder[height][idx]:
            idx += 1
    return idx


def simul(ladder):
    for i in range(n):
        if i != run(ladder, i):
            return False
    return True


def dfs(ladder, x=0, y=0, depth=1):
    global answer

    if depth == 4:
        return

    if x >= h or y >= n - 1:
        return

    ###### 이 부분에서 실수함.
    for j in range(y, n - 1):
        if ladder[x][j] == 1:
            continue
        if j > 0 and ladder[x][j - 1] == 1:
            continue
        if j < n - 2 and ladder[x][j + 1] == 1:
            continue
        ladder[x][j] = 1

        if simul(ladder):
            answer = min(answer, depth)

        nx = x + int(j + 1 == n - 1)
        ny = (j + 1) % (n - 1)

        dfs(ladder, nx, ny, depth + 1)
        ladder[x][j] = 0

    for i in range(x, h):
        for j in range(0, n - 1):
            if ladder[i][j] == 1:
                continue
            if j > 0 and ladder[i][j - 1] == 1:
                continue
            if j < n - 2 and ladder[i][j + 1] == 1:
                continue
            ladder[i][j] = 1

            if simul(ladder):
                answer = min(answer, depth)

            nx = i + int(j + 1 == n - 1)
            ny = (j + 1) % (n - 1)

            dfs(ladder, nx, ny, depth + 1)
            ladder[i][j] = 0


if __name__ == "__main__":
    n, m, h = map(int, input().split())
    ladder = [[0] * (n - 1) for _ in range(h)]
    answer = 10
    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a - 1][b - 1] = 1

    if simul(ladder):
        answer = 0
    else:
        dfs(ladder)

    print(-1 if answer > 3 else answer)
