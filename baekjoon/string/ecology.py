# https://www.acmicpc.net/problem/4358

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

hash = defaultdict(int)
total = 0
while 1:
    tree = input()
    if not tree:
        break
    hash[tree] += 1
    total += 1

result = []
for key, val in hash.items():
    result.append((key, (val / total) * 100))
result.sort()

for name, pro in result:
    print("{} {:.4f}".format(name, pro))
