# https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 코딩테스트 고득점 Kit : binary search


def solution(distance, rocks, n):
    def f(x):
        prev = 0
        removed = 0
        for rock in rocks:
            if rock - prev < x:
                removed += 1
            else:
                prev = rock

        return removed

    rocks.sort()
    rocks.append(distance)

    left = 0
    right = distance + 1
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if f(mid) > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer
