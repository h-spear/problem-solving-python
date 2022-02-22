# https://programmers.co.kr/learn/courses/30/lessons/87946


def dfs(k, dungeons, visited, ans, depth=0):
    global answer
    if sum(visited) == len(dungeons):
        ans[0] = len(dungeons)
        return

    next = False
    for i, (req, con) in enumerate(dungeons):
        if k < req:
            continue
        if visited[i]:
            continue
        next = True
        k -= con
        visited[i] = 1
        dfs(k, dungeons, visited, ans, depth + 1)
        visited[i] = 0
        k += con

    if next == False:
        ans[0] = max(ans[0], depth)


def solution(k, dungeons):
    visited = [0] * len(dungeons)
    answer = [0]
    dfs(k, dungeons, visited, answer)
    return answer[0]
