# https://school.programmers.co.kr/learn/courses/30/lessons/60062
# https://tech.kakao.com/2019/10/02/kakao-blind-recruitment-2020-round1/
# https://www.youtube.com/watch?v=yYc2KiCSIoA
# very hard
# brute force + permutation

from itertools import permutations


def solution(n, weak, dist):
    weak_size = len(weak)
    dist_size = len(dist)
    for i in range(weak_size):
        weak.append(weak[i] + n)

    INF = float("inf")
    min_cnt = INF

    for start in range(weak_size):
        for d in permutations(dist, dist_size):
            cnt = 1
            pos = start

            for i in range(1, weak_size):
                next_pos = start + i
                diff = weak[next_pos] - weak[pos]
                if diff > d[cnt - 1]:
                    pos = next_pos
                    cnt += 1
                    if cnt > dist_size:
                        break

            if cnt <= dist_size:  #####
                min_cnt = min(min_cnt, cnt)

    if min_cnt == INF:
        return -1

    return min_cnt
