import sys


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
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, n + 1):
        if input_data[j - 1] == 1:
            union(parent, i, j)


def isPossible(itinerary):
    for x in itinerary:
        if find(parent, itinerary[0]) != find(parent, x):
            print("NO")
            return
    print("YES")


isPossible(list(map(int, input().split())))
