# https://www.acmicpc.net/problem/5568

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
k = int(input())
nums = [input() for _ in range(n)]
perm = [None] * k
visited = [False] * n
s = set()


def dfs(depth):
    if depth == k:
        s.add("".join(perm))
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        perm[depth] = nums[i]
        dfs(depth + 1)
        visited[i] = False


dfs(0)
print(len(s))
