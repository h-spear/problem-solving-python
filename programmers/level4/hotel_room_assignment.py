# https://school.programmers.co.kr/learn/courses/30/lessons/64063


def solution(k, room_number):
    answer = []
    room = dict()

    for rn in room_number:
        if rn not in room:
            room[rn] = rn + 1
            answer.append(rn)
            continue

        ### 효율성
        path = []
        while rn in room:
            path.append(rn)
            rn = room[rn]

        for i, p in enumerate(path):
            room[p] = rn + 1
        ###

        room[rn] = rn + 1
        answer.append(rn)

    return answer
