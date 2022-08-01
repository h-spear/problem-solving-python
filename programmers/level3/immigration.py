# https://school.programmers.co.kr/learn/courses/30/lessons/43238


def solution(n, times):
    def func(t):
        temp = 0
        for time in times:
            temp += t // time
        return temp

    answer = 0
    left = 0
    right = int(1e18)

    while left <= right:
        mid = (left + right) // 2

        t = func(mid)
        if t >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer
