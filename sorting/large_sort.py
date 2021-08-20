# https://www.acmicpc.net/problem/10989

import sys

numbers=[0] * 10001
n = int(input())

for _ in  range(n):
  input_data = int(sys.stdin.readline())
  numbers[input_data] += 1

used= []
for i in range(1,10001):
  if numbers[i] != 0:
    used.append(i)

for i in used:
  for _ in range(numbers[i]):
    print(i)
