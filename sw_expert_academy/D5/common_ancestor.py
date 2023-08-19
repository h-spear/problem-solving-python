# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&problemLevel=7&problemLevel=8&contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=8&pageSize=10&pageIndex=1


def count_subtree(node):
    if len(child[node]) == 0:
        return 1

    temp = 1
    for c in child[node]:
        temp += count_subtree(c)
    return temp


T = int(input())
for test_case in range(1, T + 1):
    V, E, A, B = map(int, input().split())
    edge_info = list(map(int, input().split()))
    child = [[] for _ in range(V + 1)]
    parent = [None] * (V + 1)

    for i in range(0, len(edge_info), 2):
        p, c = edge_info[i], edge_info[i + 1]
        child[p].append(c)
        parent[c] = p

    checker = [False] * (V + 1)

    curr = A
    while curr:
        checker[curr] = True
        curr = parent[curr]

    curr = B
    while curr:
        if checker[curr]:
            break
        curr = parent[curr]

    print(f"#{test_case} {curr} {count_subtree(curr)}")
