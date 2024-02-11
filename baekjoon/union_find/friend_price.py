# https://www.acmicpc.net/problem/16562


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    A[b] = min(A[b], A[a])
    A[a] = min(A[b], A[a])
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m, k = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0, 0)
parent = [i for i in range(n + 1)]
for _ in range(m):
    v, w = map(int, input().split())
    union(parent, v, w)

answer = 0
for i in range(1, n + 1):
    if find(parent, 0) == find(parent, i):
        continue
    answer += A[i]
    union(parent, 0, i)

if answer <= k:
    print(answer)
else:
    print("Oh no")
