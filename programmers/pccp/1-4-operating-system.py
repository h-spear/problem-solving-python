# https://school.programmers.co.kr/learn/courses/15008/lessons/121686

import heapq


def solution(program):
    answer = [0] * 11
    program.sort(key=lambda x: -x[1])
    t = 0
    heap = []
    while program or heap:
        while program and program[-1][1] <= t:
            heapq.heappush(heap, program.pop())

        if not heap and program:
            t = program[-1][1]
        else:
            a, b, c = heapq.heappop(heap)
            answer[a] += t - b
            t += c

    answer[0] = t
    return answer
