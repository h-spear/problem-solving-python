# https://www.acmicpc.net/problem/1671


def dfs(i):
    if visited[i]:
        return False
    visited[i] = True

    for x in graph[i]:
        if not eaten[x] or dfs(eaten[x]):
            eaten[x] = i
            return True

    return False


count = 0
n = int(input())
stat = [None] * (n + 1)
eaten = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    stat[i] = tuple(map(int, input().split()))

for i in range(1, n):
    for j in range(i + 1, n + 1):
        ## 능력치가 같으면 인덱스가 작은 상어가 잡아먹는다.
        if (
            stat[i][0] == stat[j][0]
            and stat[i][1] == stat[j][1]
            and stat[i][2] == stat[j][2]
        ):
            graph[i].append(j)
        if (
            stat[i][0] >= stat[j][0]
            and stat[i][1] >= stat[j][1]
            and stat[i][2] >= stat[j][2]
        ):
            graph[i].append(j)
        elif (
            stat[i][0] <= stat[j][0]
            and stat[i][1] <= stat[j][1]
            and stat[i][2] <= stat[j][2]
        ):
            graph[j].append(i)

for _ in range(2):
    for i in range(1, n + 1):
        visited = [0] * (n + 1)
        if dfs(i):
            count += 1

print(n - count)
