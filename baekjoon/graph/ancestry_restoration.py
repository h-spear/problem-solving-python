# https://www.acmicpc.net/problem/21276

from collections import defaultdict, deque

n = int(input())
people = list(input().split())
m = int(input())
graph = defaultdict(list)
in_degree = defaultdict(int)
for _ in range(m):
    a, b = input().split()
    graph[b].append(a)
    in_degree[a] += 1

people.sort()


def topology_sort():
    root = []
    child = defaultdict(list)
    for p in people:
        if p not in in_degree:
            root.append(p)

    for i in range(len(root)):
        q = deque([root[i]])
        while q:
            x = q.popleft()
            for y in graph[x]:
                in_degree[y] -= 1
                if in_degree[y] == 0:
                    child[x].append(y)
                    q.append(y)

    print(len(root))
    print(" ".join(sorted(root)))
    for p in people:
        if p not in child:
            print(p, 0)
        else:
            print(p, len(child[p]), " ".join(sorted(child[p])))


topology_sort()
