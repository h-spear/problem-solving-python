# https://school.programmers.co.kr/learn/courses/30/lessons/150365

from collections import deque


def solution(n, m, x, y, r, c, k):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    dist_src_to_dest = abs(x - r) + abs(y - c)
    dist_src_to_DL = abs(n - x) + abs(y - 1)
    dist_DL_to_dest = abs(n - r) + abs(c - 1)
    dist_dest_to = [[-1] * (m + 1) for _ in range(n + 1)]

    if dist_src_to_dest > k:
        return "impossible"

    # bfs
    q = deque([(r, c)])
    dist_dest_to[r][c] = 0
    while q:
        _r, _c = q.popleft()
        for i in range(4):
            nr = _r + dr[i]
            nc = _c + dc[i]

            if nr <= 0 or nc <= 0 or nr > n or nc > m:
                continue
            if dist_dest_to[nr][nc] != -1:
                continue
            dist_dest_to[nr][nc] = dist_dest_to[_r][_c] + 1
            q.append((nr, nc))

    answer = ""
    if dist_src_to_DL + dist_DL_to_dest > k:
        _k, _x, _y = k, x, y

        while dist_dest_to[_x][_y] < _k:
            if _x < n:
                _x += 1
                answer += "d"
            elif _y > 1:
                _y -= 1
                answer += "l"
            _k -= 1

        if c < _y:
            answer += "l" * (_y - c)
        else:
            answer += "r" * (c - _y)

        answer += "u" * abs(r - _x)

        if len(answer) > k:
            return "impossible"
    else:
        if (k - dist_src_to_DL - dist_DL_to_dest) & 1:
            return "impossible"  # 불가능

        # 일단 맨 끝가지 이동
        answer += "d" * (n - x)
        answer += "l" * (y - 1)

        # 남은 횟수는 RL 반복
        repeat = (k - dist_src_to_DL - dist_DL_to_dest) // 2
        answer += "rl" * repeat

        # 도착지점 이동
        answer += "r" * (c - 1)
        answer += "u" * (n - r)

    return answer
