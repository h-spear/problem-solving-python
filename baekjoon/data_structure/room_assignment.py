# https://www.acmicpc.net/problem/13300

from collections import defaultdict
import math

n, k = map(int, input().split())
hash = defaultdict(int)
for _ in range(n):
    s, y = map(int, input().split())
    hash[(s, y)] += 1

answer = 0
for key, val in hash.items():
    answer += math.ceil(val / k)
print(answer)
