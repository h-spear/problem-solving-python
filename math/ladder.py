# https://www.acmicpc.net/problem/2022
# 수식 : https://jinho-study.tistory.com/687
# binary search

x, y, c = map(float, input().split())


def calc(x, y, w):
    h1 = (x ** 2 - w ** 2) ** 0.5
    h2 = (y ** 2 - w ** 2) ** 0.5
    c = (h1 * h2) / (h1 + h2)
    return c


answer = 0
left = 0
right = min(x, y)
while right - left > 0.000001:
    mid = (left + right) / 2
    if calc(x, y, mid) >= c:
        left = mid
        answer = mid
    else:
        right = mid

print("%.3f" % answer)
