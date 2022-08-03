# https://school.programmers.co.kr/learn/courses/30/lessons/12952


def solution(n):
    def dfs(row):
        if n == row:
            return 1

        count = 0

        for col in range(n):
            queen[row] = col

            for i in range(row):
                if queen[i] == queen[row]:
                    break
                if abs(queen[i] - queen[row]) == abs(row - i):
                    break

            else:
                count += dfs(row + 1)
        return count

    queen = [0] * n
    return dfs(0)
