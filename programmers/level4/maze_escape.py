# https://school.programmers.co.kr/learn/courses/30/lessons/81304
# https://tech.kakao.com/2021/07/08/2021-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-for-tech-developers-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%ED%95%B4%EC%84%A4/
# dijkstra + bit mask

import heapq
from collections import defaultdict


def solution(n, start, end, roads, traps):
    def is_active_trap(x, trap):
        if x in traps and trap & 1 << trap_mapper[x]:
            return True
        return False

    def chg_trap(x, trap):
        if x not in trap_mapper:
            return trap

        i = trap_mapper[x]
        return trap ^ 1 << i

    INF = float("inf")
    graph = defaultdict(list)
    trap_mapper = {t: i for i, t in enumerate(traps)}
    traps = set(traps)
    for p, q, s in roads:
        graph[p].append((q, s, False))
        graph[q].append((p, s, True))

    # dijkstra
    distance = defaultdict(lambda: INF)
    distance[(start, 0)] = 0
    heap = []
    heapq.heappush(heap, (0, start, 0))

    while heap:
        dist, now, trap = heapq.heappop(heap)

        if now == end:
            return dist

        if dist > distance[(now, trap)]:
            continue

        now_trap = is_active_trap(now, trap)
        for _next, d, rev in graph[now]:
            next_trap = is_active_trap(_next, trap)
            cost = dist + d
            if (now_trap ^ next_trap and rev == True) or (
                now_trap == next_trap and rev == False
            ):
                new_trap = chg_trap(_next, trap)
                if distance[(_next, new_trap)] > cost:
                    distance[(_next, new_trap)] = cost
                    heapq.heappush(heap, (cost, _next, new_trap))

    return None  # can't reach
