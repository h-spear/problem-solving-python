# https://programmers.co.kr/learn/courses/30/lessons/42747
# 코딩테스트 고득점 Kit : hash

# 이진탐색을 이용하여 통과
from bisect import bisect_left


def solution(citations):
    citations.sort()
    l = len(citations)
    for h in range(max(citations), -1, -1):
        i = bisect_left(citations, h)
        if l - i >= h:
            return h


# 다른 사람의 풀이
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0
