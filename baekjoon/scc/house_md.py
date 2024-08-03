# https://www.acmicpc.net/problem/1217

import sys

sys.setrecursionlimit(40040)
input = lambda: sys.stdin.readline().rstrip()

stack = []
labels = None
finished = None
id = 0
scc_count = 0
graph = None


def main():
    global id, scc_count, graph, labels, finished

    while 1:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        sz = (M << 1) + 5
        graph = [[] for _ in range(sz)]
        labels = [0] * sz
        finished = [False] * sz
        id = 0
        scc_count = 0

        for _ in range(N):
            a, b = map(int, input().split())
            a = T(a) if a > 0 else F(-a)
            b = T(b) if b > 0 else F(-b)
            graph[NOT(a)].append(b)
            graph[NOT(b)].append(a)

        for i in range(2, sz):
            if finished[i] == False:
                dfs(i)

        all_die = True
        for i in range(1, M + 1):
            if labels[T(i)] == labels[F(i)]:
                all_die = False
                break

        print("1" if all_die else "0")


def dfs(x):
    global id, scc_count
    id += 1
    parent = labels[x] = id
    stack.append(x)

    for next in graph[x]:
        if labels[next] == 0:
            parent = min(parent, dfs(next))
        elif finished[next] == False:
            parent = min(parent, labels[next])

    if parent == labels[x]:
        while stack:
            node = stack.pop()
            finished[node] = True
            labels[node] = scc_count
            if node == x:
                break
        scc_count += 1

    return parent


def T(x):
    return x << 1


def F(x):
    return (x << 1) | 1


def NOT(x):
    return x ^ 1


if __name__ == "__main__":
    main()
