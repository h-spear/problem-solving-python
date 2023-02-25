# https://www.acmicpc.net/problem/10974

from itertools import permutations

n = int(input())
for seq in permutations(range(1, n + 1), n):
    print(*seq)
