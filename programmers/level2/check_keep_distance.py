# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

dx = [1, -1, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0]
dy = [0, 0, 1, -1, 1, -1, 1, -1, 0, 0, 2, -2]


def check_person(place, x, y):
    for i in range(12):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
            continue
        if place[nx][ny] != "P":
            continue
        if i < 4 and (nx == x or ny == y):
            return False
        if i < 8 and (place[nx][y] != "X" or place[x][ny] != "X"):
            return False
        if i >= 8 and place[(nx + x) // 2][(ny + y) // 2] != "X":
            return False
    return True


def check_keep_dist(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] != "P":
                continue
            if check_person(place, x, y):
                continue
            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check_keep_dist(place))
    return answer
