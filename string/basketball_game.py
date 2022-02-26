# https://www.acmicpc.net/problem/1159
from collections import defaultdict, Counter


n = int(input())
_dict = defaultdict(int)
for _ in range(n):
    name = input()
    _dict[name[0]] += 1

counter = Counter(_dict)
candidates = []
for alphabet, count in counter.items():
    if count >= 5:
        candidates.append(alphabet)

candidates.sort()
if candidates:
    print("".join(candidates))
else:
    print("PREDAJA")
