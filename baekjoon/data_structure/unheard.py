# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

not_hear = set()
not_see = set()

# 듣도 못한 사람
for _ in range(n):
    not_hear.add(input().rstrip())

# 보도 못한 사람
for _ in range(m):
    not_see.add(input().rstrip())

not_know = list(not_hear & not_see)
not_know.sort()

print(len(not_know))
for x in not_know:
    print(x)
