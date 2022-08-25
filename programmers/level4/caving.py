# https://school.programmers.co.kr/learn/courses/30/lessons/67260

from collections import deque, defaultdict


def solution(n, path, order):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    for x, y in order:
        in_degree[y] = x
        out_degree[x] = y

    q = deque()
    visited = [0] * n
    temp = set()
    if 0 in in_degree:
        return False
    elif 0 in out_degree:
        z = out_degree[0]
        del out_degree[0]
        del in_degree[z]
        temp.add(z)

    q.append(0)
    visited[0] = 1

    while q:
        x = q.popleft()

        for y in graph[x]:
            if visited[y]:
                continue
            if y in in_degree:
                temp.add(y)
                continue

            visited[y] = 1
            q.append(y)
            if y in out_degree:
                z = out_degree[y]
                if z in temp:
                    temp.remove(z)
                    visited[z] = 1
                    q.append(z)
                del out_degree[y]
                del in_degree[z]

    return 0 not in visited
