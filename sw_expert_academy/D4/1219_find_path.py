# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")

from collections import defaultdict, deque


def bfs(graph):
    q = deque([0])
    visited = [0] * 100
    visited[0] = 1
    while q:
        x = q.popleft()

        for y in graph[x]:
            if visited[y]:
                continue
            q.append(y)
            visited[y] = 1

    return visited[99]


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tc, n = map(int, input().split())
    nums = list(map(int, input().split()))
    graph = defaultdict(list)
    for i in range(0, len(nums), 2):
        graph[nums[i]].append(nums[i + 1])

    print(f"#{tc} {bfs(graph)}")

    # ///////////////////////////////////////////////////////////////////////////////////
