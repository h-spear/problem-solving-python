# https://school.programmers.co.kr/learn/courses/30/lessons/62050
# https://school.programmers.co.kr/learn/courses/30/lessons/62050/solution_groups?language=python3

import heapq


def solution(land, height):
    n = len(land)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    answer = 0
    max_count = n * n
    visit_count = 0
    visited = [[0] * n for _ in range(n)]

    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while heap and visit_count < max_count:
        v, x, y = heapq.heappop(heap)

        if visited[x][y]:
            continue
        visited[x][y] = 1
        answer += v

        h = land[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            nh = land[nx][ny]
            if abs(nh - h) > height:
                heapq.heappush(heap, (abs(nh - h), nx, ny))
            else:
                heapq.heappush(heap, (0, nx, ny))

    return answer
