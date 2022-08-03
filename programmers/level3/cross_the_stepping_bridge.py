# https://school.programmers.co.kr/learn/courses/30/lessons/64062


def condition(stones, k, v):
    count = 0
    for x in stones:
        if x - v <= 0:
            count += 1
        else:
            count = 0

        if count == k:
            return True

    return False


def solution(stones, k):
    left = 1
    right = max(stones)
    answer = 0
    while left <= right:
        mid = (left + right) // 2

        if condition(stones, k, mid):
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer
