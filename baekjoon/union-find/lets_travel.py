# https://www.acmicpc.net/problem/1976


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


n = int(input())
m = int(input())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(n):
    input_data = list(map(int, input().split()))
    for j, b in enumerate(input_data):
        if b == 1:
            union(parent, i + 1, j + 1)

itinerary = list(map(int, input().split()))
first = find(parent, itinerary[0])

possible = True
for i in itinerary:
    if first != find(parent, i):
        possible = False
        break

if possible:
    print("YES")
else:
    print("NO")
