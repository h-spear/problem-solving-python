# https://www.acmicpc.net/problem/15661

import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

answer = 123456789
people = set([i for i in range(n)])
for s in range(1, n // 2 + 1):
    for candidate in combinations(range(0, n), s):
        start = set(candidate)
        link = people - start

        score_start = 0
        score_link = 0

        if len(start) >= 2:
            for i, j in combinations(start, 2):
                score_start += matrix[i][j]
                score_start += matrix[j][i]

        if len(link) >= 2:
            for i, j in combinations(link, 2):
                score_link += matrix[i][j]
                score_link += matrix[j][i]

        diff = abs(score_start - score_link)
        answer = min(answer, diff)

print(answer)
