# https://www.acmicpc.net/problem/1107

import sys
from itertools import product
input = sys.stdin.readline

button = [0,1,2,3,4,5,6,7,8,9]
n = int(input().rstrip())
m = int(input().rstrip())
if m != 0:
  broken = list(map(int,input().rstrip().split()))
  for x in broken:
    button.remove(x)


# 가장 가까운 번호
def solution():
  closest = 1000000
  MIN = int(1e6)
  for i in range(1,7):
    for x in product(button,repeat=i):
      num = int("".join(list(map(str, x))))
      if abs(num - n) < MIN:
        MIN = abs(num - n)
        closest = num
  
  return min(abs(closest - n) + len(list(str(closest))), abs(n - 100))

print(solution())