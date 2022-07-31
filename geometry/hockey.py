# https://www.acmicpc.net/problem/1358

w, h, x, y, p = map(int, input().split())
r = h / 2
answer = 0


for _ in range(p):
    a, b = map(int, input().split())
    if x <= a <= x + w and y <= b <= y + h:
        answer += 1
    elif (a - x) ** 2 + (b - (y + r)) ** 2 <= r ** 2:
        answer += 1
    elif (a - (x + w)) ** 2 + (b - (y + r)) ** 2 <= r ** 2:
        answer += 1


print(answer)
