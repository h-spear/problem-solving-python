from itertools import combinations

n = int(input())
graph = []
members = [i for i in range(0, n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def stat(selected):
    stat1 = 0
    stat2 = 0
    not_selected = []
    for i in range(n):
        if i not in selected:
            not_selected.append(i)

    for x, y in combinations(selected, 2):
        stat1 += graph[x][y]
        stat1 += graph[y][x]
    for x, y in combinations(not_selected, 2):
        stat2 += graph[x][y]
        stat2 += graph[y][x]
    return abs(stat2 - stat1)


answer = 10000000
for candidate in combinations(members, len(members) // 2):
    answer = min(answer, stat(candidate))
print(answer)
