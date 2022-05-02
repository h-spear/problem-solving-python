# https://www.acmicpc.net/problem/2012

n = int(input())
order = []
for _ in range(n):
    order.append(int(input()))
order.sort()

answer = 0
for i, x in enumerate(order):
    answer += abs(i + 1 - x)

print(answer)
