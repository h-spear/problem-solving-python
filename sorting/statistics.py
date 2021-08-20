# https://www.acmicpc.net/problem/2108

import sys
n = int(input())

numbers = [0]* 8001
sum = 0
MAX, MIN = -4000,4000
for _ in range(n):
  num = int(sys.stdin.readline())
  sum += num
  MAX = max(MAX, num)
  MIN = min(MIN, num)
  numbers[num+4000] += 1

count = 0
center= 0
popular = 0
for i in range(8001):
  count += numbers[i]
  if count >= n//2+1:
    center = i-4000
    break

dict = []
for i in range(8001):
  dict.append((numbers[i],i))
dict.sort(key= lambda x:(-x[0],x[1]))

print(round(sum/n))
print(MAX if n==1 else center)
print(dict[1][1]-4000 if dict[0][0] == dict[1][0] else dict[0][1]-4000)
print(MAX-MIN)
