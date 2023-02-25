# https://www.acmicpc.net/problem/1516

from collections import defaultdict, deque

n = int(input())
time = [0] * n
in_degree = [0] * n
graph = defaultdict(list)
for i in range(n):
    input_data = list(map(int, input().split()))
    a, li = input_data[0], input_data[1:-1]
    time[i] = a
    in_degree[i] += len(li)
    for x in li:
        graph[x - 1].append(i)


q = deque()
result = [0] * n

for i in range(n):
    result[i] = time[i]
    if in_degree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()

    for y in graph[x]:
        in_degree[y] -= 1
        result[y] = max(result[y], result[x] + time[y])
        if in_degree[y] == 0:
            q.append(y)

for t in result:
    print(t)
