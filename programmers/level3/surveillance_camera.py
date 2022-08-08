# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 코딩테스트 고득점 Kit : Greedy


def solution(routes):
    routes.sort(reverse=True, key=lambda x: x[1])
    answer = 0

    while routes:
        answer += 1
        s, e = routes.pop()
        while routes:
            ss, ee = routes[-1]
            if ss <= e:
                routes.pop()
            else:
                break

    return answer
