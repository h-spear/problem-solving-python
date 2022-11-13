# https://school.programmers.co.kr/learn/courses/30/lessons/134239


def solution(k, ranges):
    lst = [k]
    while k > 1:
        if not k & 1:
            k //= 2
        else:
            k = k * 3 + 1
        lst.append(k)

    ll = len(lst)
    area = []
    for i in range(ll - 1):
        area.append(max(lst[i], lst[i + 1]) - abs(lst[i] - lst[i + 1]) / 2)

    psum = [0]
    for i in range(len(area)):
        psum.append(psum[-1] + area[i])

    answer = []
    for a, b in ranges:
        b = ll + b - 1
        if a > b:
            answer.append(-1.0)
        elif a == b:
            answer.append(0.0)
        else:
            answer.append(psum[b] - psum[a])

    return answer
