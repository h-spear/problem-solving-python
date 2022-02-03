# https://programmers.co.kr/learn/courses/30/lessons/12933


def solution(n):
    return int("".join(sorted(str(n), reverse=True)))

    # sorted로 감싸면 list로 자동으로 변환됨
    # return int("".join(sorted(list(str(n)), reverse=True)))
