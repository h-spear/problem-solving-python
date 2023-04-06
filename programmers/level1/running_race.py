# https://school.programmers.co.kr/learn/courses/30/lessons/178871


def solution(players, callings):
    playerMap = {}
    for idx, player in enumerate(players):
        playerMap[player] = idx

    for calling in callings:
        playerIdx = playerMap[calling]
        aheadIdx = playerIdx - 1
        playerMap[calling] -= 1
        playerMap[players[aheadIdx]] += 1
        players[playerIdx], players[aheadIdx] = players[aheadIdx], players[playerIdx]

    return players
