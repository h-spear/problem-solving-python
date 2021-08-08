# https://programmers.co.kr/learn/courses/30/lessons/60062
# 아직 못품
from itertools import combinations


def distance(weaks, n):
    max_weak_point = max(weaks)
    min_weak_point = min(weaks)
    difference = max_weak_point - min_weak_point
    return min(difference, n - difference)


def isCovered(weaks, dist):
    weaks.sort()
    dist.sort()

    count = 0
    temp = 0
    while dist:
        if not weaks:
            break

        temp += dist.pop()
        count += 1
        if temp >= weaks[-1]:
            temp = 0
            weaks.pop()

    return -1 if weaks else count


def solution(n, weak, dist):
    print(list(combinations(weak, 2)))

    answer = 0
    return answer


n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
