# https://www.acmicpc.net/problem/1477

import math


def func(v):
    cnt = 0

    for i in range(lr - 1):
        distance = rest_area[i + 1] - rest_area[i]
        cnt += distance // v
        if math.ceil(distance / v) == distance // v:
            cnt -= 1

    return cnt


n, m, l = map(int, input().split())
rest_area = [0]
rest_area.extend(list(map(int, input().split())))
rest_area.append(l)
rest_area.sort()

lr = len(rest_area)
left = 1
right = l + 1
while left <= right:
    mid = (left + right) // 2

    if func(mid) <= m:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
