# https://www.acmicpc.net/problem/9613

from itertools import combinations
import math  # math 라이브러리에 gcd 함수 존재


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def gcd_sum(nums: list):
    sum = 0
    for a, b in combinations(nums, 2):
        sum += math.gcd(a, b)
        # sum += gcd(a, b)
    return sum


for tc in range(int(input())):
    nums = list(map(int, input().split()))[1:]
    print(gcd_sum(nums))
