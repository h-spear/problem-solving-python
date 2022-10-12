# https://school.programmers.co.kr/learn/courses/30/lessons/131129
# dp


def solution(target):
    INF = float("inf")
    dp = [[INF, -INF] for _ in range(target + 1)]
    dp[0] = [0, 0]
    for i in range(50, target + 1, 50):
        dp[i] = [i // 50, i // 50]

    for i in range(target):
        for lv in [1, 2, 3]:
            for score in range(1, 21):
                ni = i + score * lv
                if ni > target:
                    continue
                if dp[ni][0] < dp[i][0] + 1:
                    continue
                if dp[ni][0] == dp[i][0] + 1 and dp[ni][1] >= dp[i][1] + (
                    1 if lv == 1 else 0
                ):
                    continue
                dp[ni] = [dp[i][0] + 1, dp[i][1] + (1 if lv == 1 else 0)]

    return dp[target]
