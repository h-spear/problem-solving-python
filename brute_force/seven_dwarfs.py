# https://www.acmicpc.net/problem/2309

from itertools import combinations

height = []
for _ in range(9):
    height.append(int(input()))

for candidate in combinations(height, 7):
    if sum(candidate) == 100:
        for x in sorted(candidate):
            print(x)
        break
