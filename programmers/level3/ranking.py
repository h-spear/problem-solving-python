# https://programmers.co.kr/learn/courses/30/lessons/49191
# 코딩테스트 고득점 Kit : graph


def solution(n, results):
    INF = float("inf")
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = 1

    answer = 0
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            if graph[i][j] == 1 or graph[j][i] == 1:
                cnt += 1

        if cnt == n - 1:
            answer += 1

    return answer
