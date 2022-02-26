# https://www.acmicpc.net/problem/13022

import re

s = input()

for i in range(1, 14):
    pattern = re.compile(
        r"w{"
        + str(i)
        + r"}"
        + r"o{"
        + str(i)
        + r"}"
        + r"l{"
        + str(i)
        + r"}"
        + r"f{"
        + str(i)
        + r"}"
    )
    s = re.sub(pattern, "!", s)

s = re.sub("!", "", s)

if s:
    print(0)
else:
    print(1)
