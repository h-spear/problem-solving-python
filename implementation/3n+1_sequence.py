# https://www.acmicpc.net/problem/14920

import sys


c = int(input())
n = 1

if c == 1:
    print(1)
    sys.exit()

while True:
    if c & 1:  # 홀수
        c = 3 * c + 1
    else:
        c //= 2

    n += 1
    if c == 1:
        break

print(n)
