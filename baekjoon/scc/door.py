# https://www.acmicpc.net/problem/2416

import sys

sys.setrecursionlimit(500000)
input = lambda: sys.stdin.readline().rstrip()

stack = None
graph = None
labels = None
finished = None
id = 0
sz = 0


def main():
    global id, stack, graph, labels, finished
    N, M = map(int, input().split())

    count_of_nodes = (M << 1) + 2
    stack = []
    graph = [[] for _ in range(count_of_nodes)]
    labels = [-1] * count_of_nodes
    finished = [False] * count_of_nodes

    for _ in range(N):
        a, sa, b, sb = map(int, input().split())
        a = T(a) if sa == 1 else F(a)
        b = T(b) if sb == 1 else F(b)
        graph[NOT(a)].append(b)
        graph[NOT(b)].append(a)

    for i in range(2, count_of_nodes):
        if not finished[i]:
            dfs(i)

    valid = True
    for i in range(1, M + 1):
        if labels[T(i)] == labels[F(i)]:
            valid = False
            break

    if not valid:
        print("IMPOSSIBLE")
    else:
        result = []
        for i in range(1, M + 1):
            result.append(int(labels[T(i)] < labels[F(i)]))
        print(*result, sep="\n")


def dfs(x):
    global id, sz
    id += 1
    parent = labels[x] = id
    stack.append(x)

    for next in graph[x]:
        if labels[next] == -1:
            parent = min(parent, dfs(next))
        elif not finished[next]:
            parent = min(parent, labels[next])

    if parent == labels[x]:
        while stack:
            node = stack.pop()
            labels[node] = sz
            finished[node] = True
            if node == x:
                break
        sz += 1

    return parent


def T(x):
    return x << 1


def F(x):
    return (x << 1) | 1


def NOT(x):
    return x ^ 1


if __name__ == "__main__":
    main()
