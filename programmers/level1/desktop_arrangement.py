# https://school.programmers.co.kr/learn/courses/30/lessons/161990


def solution(wallpaper):
    answer = [1000, 1000, -1, -1]
    n = len(wallpaper)
    m = len(wallpaper[0])
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j] == "#":
                answer[0] = min(answer[0], i)
                answer[1] = min(answer[1], j)
                answer[2] = max(answer[2], i + 1)
                answer[3] = max(answer[3], j + 1)

    return answer
