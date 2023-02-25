# https://www.acmicpc.net/problem/2168
# 대각선 타일의 개수 : x + y - gcd(x,y)

import math

x, y = map(int, input().split())
print(x + y - math.gcd(x, y))
