# https://programmers.co.kr/learn/courses/30/lessons/42579
# 코딩테스트 고득점 Kit : hash

from collections import defaultdict
import heapq


def solution(genres, plays):
    _dict = defaultdict(list)
    counter = defaultdict(int)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        heapq.heappush(_dict[genre], (-play, i))
        counter[genre] += play

    answer = []
    counter = sorted(counter.items(), key=lambda x: -x[1])
    print(counter)
    print(_dict)
    for key, _ in counter:
        for i in range(2):
            if not _dict[key]:
                continue
            _, i = heapq.heappop(_dict[key])
            answer.append(i)
    return answer
