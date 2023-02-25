# https://www.acmicpc.net/problem/2688
# 중복조합
import math

for t in range(int(input())):
    n = int(input())
    print(math.comb(9 + n, n))
