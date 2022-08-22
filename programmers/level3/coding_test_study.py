# https://school.programmers.co.kr/learn/courses/30/lessons/118668
# https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/

g_problems = None
tar_alp = 0
tar_cop = 0
INF = 1000
answer = INF
dp = None


def dfs(alp, cop):
    alp = min(tar_alp, alp)
    cop = min(tar_cop, cop)

    if dp[alp][cop] != INF:
        return dp[alp][cop]

    dp[alp][cop] = INF + 1
    dp[alp][cop] = min(dp[alp][cop], dfs(alp + 1, cop) + 1)
    dp[alp][cop] = min(dp[alp][cop], dfs(alp, cop + 1) + 1)

    for alp_req, cop_req, alp_rwd, cop_rwd, cost in g_problems:
        if alp < alp_req:
            continue
        if cop < cop_req:
            continue
        dp[alp][cop] = min(dp[alp][cop], dfs(alp + alp_rwd, cop + cop_rwd) + cost)

    return dp[alp][cop]


def solution(alp, cop, problems):
    global g_problems, tar_alp, tar_cop, answer, dp

    g_problems = problems
    for alp_req, cop_req, _, _, _ in problems:
        tar_alp = max(tar_alp, alp_req)
        tar_cop = max(tar_cop, cop_req)
    dp = [[INF] * (tar_cop + 1) for _ in range(tar_alp + 1)]
    dp[tar_alp][tar_cop] = 0
    alp = min(tar_alp, alp)
    cop = min(tar_cop, cop)

    return dfs(alp, cop)
