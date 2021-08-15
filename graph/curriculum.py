from collections import deque
import copy

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0]

for i in range(1, n + 1):
    input_data = list(map(int, input().split()))
    time.append(input_data[0])
    for prerequisite in input_data[1:-1]:
        graph[prerequisite].append(i)
        indegree[i] += 1


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
        print(result)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()
