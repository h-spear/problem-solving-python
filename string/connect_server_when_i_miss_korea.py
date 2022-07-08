# https://www.acmicpc.net/problem/9996
# .(dot) : \n을 제외한 모든 문자와 매치

import re

n = int(input())
p1, p2 = input().split("*")
p = p1 + ".*" + p2
pattern = re.compile(p)
for _ in range(n):
    s = input()
    m = pattern.fullmatch(s)
    if m:
        print("DA")
    else:
        print("NE")
