# https://www.acmicpc.net/problem/9663
# 참고 : https://junior-datalist.tistory.com/89?category=866196


def check(queen: list, row: int) -> bool:
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False
    return True


def dfs(queen: list, row: int) -> int:
    global n
    cnt = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        if check(queen, row):
            cnt += dfs(queen, row + 1)

    return cnt


def solution(n: int) -> int:
    return dfs([0] * n, 0)


n = int(input())
print(solution(n))
