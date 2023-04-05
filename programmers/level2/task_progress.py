# https://school.programmers.co.kr/learn/courses/30/lessons/176962

from collections import deque


def timeToNumber(time):
    splited = time.split(":")
    return int(splited[0]) * 60 + int(splited[1])


def solution(plans):
    plans = [
        [name, timeToNumber(start), int(playtime)] for name, start, playtime in plans
    ]
    plans.sort(key=lambda x: x[1])
    plans = deque(plans)

    stack = []
    answer = []

    while plans:
        name, start, playtime = plans.popleft()
        end = start + playtime

        if plans:
            if plans[0][1] == end:
                answer.append(name)
                print(3)
            elif plans[0][1] > end:
                print(2)
                answer.append(name)
                if stack:
                    name, remainder = stack.pop()
                    plans.appendleft([name, end, remainder])
            else:
                remainder = playtime - (plans[0][1] - start)
                print(1, remainder)
                stack.append((name, remainder))
        else:
            answer.append(name)

    while stack:
        answer.append(stack.pop()[0])

    return answer
