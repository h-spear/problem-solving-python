# https://www.acmicpc.net/problem/17352

n = int(input())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(n - 2):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, n + 1):
    if find(parent[i]) != parent[1]:
        print(parent[1], find(parent[i]))
        break
