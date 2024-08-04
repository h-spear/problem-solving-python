# https://www.acmicpc.net/problem/15203

import sys

sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

scc = None
stack = None
graph = None
labels = None
finished = None
N = -1
id = -1


def main():
    global N, id, stack, graph, labels, scc, finished
    N, M = map(int, input().split())

    id = 0
    scc = []
    stack = []
    graph = [[] for _ in range(N + 1)]
    labels = [-1] * (N + 1)
    finished = [False] * (N + 1)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)

    for i in range(1, N + 1):
        if not finished[i]:
            dfs(i)

    sz = len(scc)
    scc_in_degree = [0] * sz
    for i in range(1, N + 1):
        for j in graph[i]:
            if labels[i] != labels[j]:
                scc_in_degree[labels[j]] += 1

    count = 0
    index = 0
    for i in range(sz):
        if scc_in_degree[i] == 0:
            count += 1
            index = i

    if count == 1:
        scc[index].sort()
        print(len(scc[index]))
        print(" ".join(map(str, scc[index])))
    else:
        print("0\n")


def dfs(x):
    global id
    id += 1
    parent = labels[x] = id
    stack.append(x)

    for next in graph[x]:
        if labels[next] == -1:
            parent = min(parent, dfs(next))
        elif not finished[next]:
            parent = min(parent, labels[next])

    if parent == labels[x]:
        component = []
        s = len(scc)
        while stack:
            node = stack.pop()
            labels[node] = s
            finished[node] = True
            component.append(node)
            if node == x:
                break
        scc.append(component)
    return parent


if __name__ == "__main__":
    main()
