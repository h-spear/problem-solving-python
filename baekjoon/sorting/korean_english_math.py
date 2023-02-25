# https://www.acmicpc.net/problem/10825

import sys

n = int(input())
data = []
for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().rstrip().split()
    data.append([name, int(kor), int(eng), int(math)])

data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, kor, eng, math in data:
    print(name)
