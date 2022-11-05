# https://blog.goorm.io/hyundaimobis_preliminary/5/
# 2022 현대모비스 알고리즘 경진대회 예선 문제 4

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
res = []
counter = defaultdict(int)
_hash = {}

n = int(input())
for _ in range(n):
    op = input()
    counter[op] += 1

k = int(input())
for _ in range(k):
    res.append(input())

set_res = set(res)

for op in counter.keys():
    lo = len(op)
    for i in range(lo):
        prefix = op[: i + 1]
        if prefix not in set_res:
            continue

        if prefix not in _hash:
            _hash[prefix] = op
        else:
            now = _hash[prefix]
            if counter[now] < counter[op]:
                _hash[prefix] = op
            elif counter[now] == counter[op] and op < now:
                _hash[prefix] = op

for key in res:
    if key not in _hash:
        print(0)
    else:
        value = _hash[key]
        print(value, counter[value])
