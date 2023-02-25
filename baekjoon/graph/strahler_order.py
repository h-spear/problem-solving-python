# https://www.acmicpc.net/problem/9470

from collections import defaultdict, deque

for tc in range(1, int(input()) + 1):

    k, m, p = map(int, input().split())
    graph = defaultdict(list)
    in_degree = [0] * (m + 1)
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    def topology_sort():
        q = deque()
        result = [0] * (m + 1)
        c = defaultdict(list)
        for i in range(1, m + 1):
            if in_degree[i] == 0:
                q.append(i)
                result[i] = 1

        while q:
            x = q.popleft()

            for y in graph[x]:
                in_degree[y] -= 1
                c[y].append(result[x])

                if in_degree[y] == 0:
                    i = max(c[y])
                    if c[y].count(i) >= 2:
                        result[y] = max(result[y], i + 1)
                    else:
                        result[y] = max(result[y], i)
                    q.append(y)

        print(tc, result[m])

    topology_sort()
