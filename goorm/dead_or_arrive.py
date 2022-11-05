# https://blog.goorm.io/hyundaimobis_preliminary/2/
# 2022 현대모비스 알고리즘 경진대회 예선 문제 1

from collections import defaultdict

n = int(input())
_hash = defaultdict(list)
for i in range(1, n + 1):
    v, w = map(int, input().split())
    _hash[v].append((w, i))

answer = 0
for k in _hash:
    cars = _hash[k]
    cars.sort(reverse=True)
    answer += cars[0][1]

print(answer)
