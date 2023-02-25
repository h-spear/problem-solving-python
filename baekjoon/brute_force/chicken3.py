# https://www.acmicpc.net/problem/16439

from itertools import combinations

n, m = map(int, input().split())
preference = []
for _ in range(n):
    preference.append(list(map(int, input().split())))

answer = 0
for a, b, c in combinations(range(m), 3):
    score = 0
    for member in range(n):
        p = preference[member]
        score += max(p[a], p[b], p[c])
    answer = max(answer, score)

print(answer)
