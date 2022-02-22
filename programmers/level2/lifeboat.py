# https://programmers.co.kr/learn/courses/30/lessons/42885
# 코딩테스트 고득점 Kit : greedy
# 두 명만 탑승할 수 있으므로 가장 무게가 큰 사람과 작은 사람이 limit를 넘는지를 체크함.

from collections import deque


def solution(people, limit):
    answer = 0
    people = deque(sorted(people))

    while people:
        if len(people) == 1:
            people.pop()
            answer += 1
            break

        if people[0] + people[-1] > limit:
            people.pop()
            answer += 1
        else:
            people.popleft()
            people.pop()
            answer += 1

    return answer
