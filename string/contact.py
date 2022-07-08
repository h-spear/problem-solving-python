# https://www.acmicpc.net/problem/1013
# 정규표현식 fullmatch, | 등...

import re

for tc in range(int(input())):
    s = input()
    pattern = re.compile("(100+1+|01)+")
    m = pattern.fullmatch(s)

    if m:
        print("YES")
    else:
        print("NO")
