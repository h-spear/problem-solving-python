# https://www.acmicpc.net/problem/1182

from itertools import combinations

n, s = map(int, input().split())
a = list(map(int, input().split()))

answer = 0
for i in range(1, len(a) + 1):
    for candidate in combinations(a, i):
        total = sum(candidate)
        if total == s:
            answer += 1

print(answer)
