# https://www.acmicpc.net/problem/1977

import math

m = int(input())
n = int(input())

minimum = 0
total_sum = 0

isExist = False

i = math.floor(math.sqrt(n))
while 1:
    now = i ** 2
    if now < m:
        break

    total_sum += now
    minimum = now
    i -= 1
    isExist = True

if isExist:
    print(total_sum)
    print(minimum)
else:
    print(-1)
