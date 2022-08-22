# https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(q1)
    sum_q2 = sum(q2)
    len_q1 = len(q1)
    len_q2 = len(q2)
    summ = sum_q1 + sum_q2

    if summ & 1:
        return -1

    bo = summ // 2
    cnt = 0
    while sum_q1 != sum_q2:
        if sum_q1 > sum_q2:
            val = q1.popleft()
            q2.append(val)
            sum_q1 -= val
            sum_q2 += val
        else:
            val = q2.popleft()
            q1.append(val)
            sum_q2 -= val
            sum_q1 += val

        cnt += 1
        if cnt >= 2 * (len_q1 + len_q2):
            return -1

    return cnt
