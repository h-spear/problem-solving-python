# https://school.programmers.co.kr/learn/courses/30/lessons/147354


def solution(data, col, row_begin, row_end):
    answer = 0

    data.sort(key=lambda x: (x[col - 1], -x[0]))
    for row in range(row_begin - 1, row_end):
        s = 0
        for element in data[row]:
            s += element % (row + 1)
        answer ^= s

    return answer
