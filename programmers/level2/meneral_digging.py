# https://school.programmers.co.kr/learn/courses/30/lessons/172927

m, answer = 0, 9876543210
gPicks = None
gMinerals = None
gTable = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
mineralMap = {"diamond": 0, "iron": 1, "stone": 2}


def dfs(route):
    global answer

    # 모든 광물을 채취할 수 있거나, 모든 곡괭이를 다 사용하였을 때
    if len(route) * 5 >= m or sum(gPicks) == 0:
        answer = min(answer, get_piro(route))
        return

    for i in range(3):
        if gPicks[i]:
            route.append(i)
            gPicks[i] -= 1
            dfs(route)
            gPicks[i] += 1
            route.pop()


def get_piro(route):
    piro = 0
    mIdx = 0
    for pick in route:
        for i in range(5):
            if mIdx < m:
                piro += gTable[pick][gMinerals[mIdx]]
                mIdx += 1
    return piro


def solution(picks, minerals):
    global m, answer, gPicks, gMinerals
    minerals = [mineralMap[mineral] for mineral in minerals]
    m = len(minerals)
    gPicks = picks
    gMinerals = minerals
    dfs([])
    return answer
