# https://www.acmicpc.net/problem/17219

import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
dic = dict()
for _ in range(n):
    site, pwd = input().rstrip().split()
    dic[site] = pwd

for _ in range(m):
    want = input().rstrip()
    print(dic[want])
