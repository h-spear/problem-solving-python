# https://www.acmicpc.net/problem/2792

import math

n, m = map(int, input().split())
jewelry_box = []
for _ in range(m):
    jewelry_box.append(int(input()))


def func(jealousy):
    cnt = 0
    for jewel in jewelry_box:
        cnt += math.ceil(jewel / jealousy)

    return cnt


left = 1
right = int(1e9)
answer = 0
while left <= right:
    mid = (left + right) // 2

    cnt = func(mid)
    if cnt <= n:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1


print(answer)
