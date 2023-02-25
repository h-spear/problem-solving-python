# https://www.acmicpc.net/problem/20040


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


parent = [0] * 500001
for i in range(1, 500001):
    parent[i] = i

n, m = map(int, input().split())
progress = []
for _ in range(m):
    progress.append(list(map(int, input().split())))

end = False
for i, now in enumerate(progress):
    a, b = now
    if find(parent, a) == find(parent, b):
        end = True
        break
    union(parent, a, b)

if end:
    print(i + 1)
else:
    print(0)
