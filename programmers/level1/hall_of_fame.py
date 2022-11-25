# https://school.programmers.co.kr/learn/courses/30/lessons/138477


def solution(k, score):
    n = len(score)
    q = []
    answer = []
    for x in score:
        if len(q) >= k:
            q.sort(reverse=True)
            if q[-1] > x:
                answer.append(q[-1])
                continue
            q.pop()

        q.append(x)
        answer.append(min(q))

    return answer
