# https://programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    max_h, max_w = 0, 0
    for w, h in sizes:
        if h < w:
            h, w = w, h
        max_h = max(h, max_h)
        max_w = max(w, max_w)
    return max_h * max_w


###############################
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)
