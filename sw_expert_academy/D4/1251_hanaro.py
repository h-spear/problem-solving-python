# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AV15StKqAQkCFAYD&categoryId=AV15StKqAQkCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=1

# import sys
# sys.stdin = open("input.txt", "r")


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


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    parent = [i for i in range(n + 1)]
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
            edges.append((e * dist, i, j))

    edges.sort()
    result = 0
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue
        union(parent, a, b)
        result += c

    print(f"#{test_case} {int(round(result, 0))}")
    # ///////////////////////////////////////////////////////////////////////////////////
