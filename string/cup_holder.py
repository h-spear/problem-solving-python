# https://www.acmicpc.net/problem/2810

import re

n = int(input())
seat = input()
seat = re.sub("S", "*S*", seat)
seat = re.sub("LL", "*LL*", seat)
seat = re.sub("\*+", "*", seat)
print(min(n, seat.count("*")))
