# https://www.acmicpc.net/problem/3009

from collections import defaultdict

x = defaultdict(int)
y = defaultdict(int)
for _ in range(3):
    coord_x, coord_y = map(int, input().split())
    x[coord_x] += 1
    y[coord_y] += 1

for key in x:
    if x[key] == 1:
        print(key, end=" ")

for key in y:
    if y[key] == 1:
        print(key)
