# https://www.acmicpc.net/problem/11403

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, (input().split()))))

result = [[0] * n for _ in range(n)]


def dfs(i):
    visited = [False] * n
    list = [i]

    while list:
        node = list.pop()
        for j in range(n):
            if graph[node][j] == 1 and visited[j] == False:
                visited[j] = True
                result[i][j] = 1
                list.append(j)


for i in range(n):
    dfs(i)

for row in result:
    for x in row:
        print(x, end=" ")
    print()
