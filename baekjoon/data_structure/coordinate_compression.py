# https://www.acmicpc.net/problem/18870

import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().rstrip().split()))

order = sorted(list(set(data)))
dic = dict()
for i in range(len(order)):
    dic[order[i]] = i

for x in data:
    print(dic[x], end=" ")
