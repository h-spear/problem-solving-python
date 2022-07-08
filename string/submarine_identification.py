# https://www.acmicpc.net/problem/2671

import re

s = input()
pattern = re.compile("(100+1+|01)+")
m = pattern.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")
