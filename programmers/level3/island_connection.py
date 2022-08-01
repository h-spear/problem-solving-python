# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 코딩테스트 고득점 Kit : greedy


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


def solution(n, costs):
    parent = [i for i in range(n + 1)]
    edges = []
    for a, b, c in costs:
        edges.append((c, a, b))

    edges.sort()

    answer = 0
    for c, a, b in edges:
        if find(parent, a) == find(parent, b):
            continue

        union(parent, a, b)
        answer += c

    return answer
