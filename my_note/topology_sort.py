import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
in_degree = [0] * (n + 1)
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1


# for문 사용
def topology_sort():
    result = []
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    # 위상 정렬이 완전히 수행되려면 정확히 n개의 노드를 방문함.
    for i in range(n):
        # q가 비었다면 사이클이 발생한 것
        if not q:
            print("Cycle")
            break

        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)

    for i in result:
        print(i, end=" ")


# while q 사용
def topology_sort():
    result = []
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for next in graph[now]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)

    for i in result:
        print(i, end=" ")


topology_sort()
