# https://www.acmicpc.net/problem/21924


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]
answer = 0
cnt = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    answer += c

edges.sort()
for c, a, b in edges:
    if find(parent, a) == find(parent, b):
        continue

    union(parent, a, b)
    answer -= c
    cnt += 1

if cnt == n - 1:
    print(answer)
else:
    print(-1)
