# https://www.acmicpc.net/problem/2623

from collections import deque, defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
in_degree = [0] * (n + 1)

for _ in range(m):
    input_data = list(map(int, input().split()))
    l, li = input_data[0], input_data[1:]
    for i in range(l - 1):
        graph[li[i]].append(li[i + 1])
        in_degree[li[i + 1]] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    for i in range(1, n + 1):
        if len(q) == 0:
            print(0)
            return

        x = q.popleft()
        result.append(x)
        for y in graph[x]:
            in_degree[y] -= 1
            if in_degree[y] == 0:
                q.append(y)

    for x in result:
        print(x)


topology_sort()
