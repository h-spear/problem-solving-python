# https://www.acmicpc.net/problem/1436

import sys

input = sys.stdin.readline
n = int(input())

def check(num):
  c = str(num)
  return '666' in c

array = []
num = 0
cnt = 0
while True:
  if check(num):
    cnt += 1
  
  if cnt == n:
    print(num)
    break
  num += 1
