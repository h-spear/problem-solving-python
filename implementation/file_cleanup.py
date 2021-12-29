# https://www.acmicpc.net/problem/20291

from collections import defaultdict
import sys

input = lambda: sys.stdin.readline().rstrip()

_dict = defaultdict(int)
n = int(input())
for _ in range(n):
    file = input()
    extension = file[file.index(".") + 1 :]
    _dict[extension] += 1

q = []
for key in _dict:
    q.append((key, _dict[key]))
q.sort()

for ext, num in q:
    print(ext, num)
