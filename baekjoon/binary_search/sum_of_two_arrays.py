# https://www.acmicpc.net/problem/2143

from bisect import bisect_left, bisect_right


t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

acc_a = []
acc_b = []

for i in range(n):
    summ = a[i]
    acc_a.append(summ)
    for j in range(i + 1, n):
        summ += a[j]
        acc_a.append(summ)

for i in range(m):
    summ = b[i]
    acc_b.append(summ)
    for j in range(i + 1, m):
        summ += b[j]
        acc_b.append(summ)

acc_b.sort()

answer = 0
for x in acc_a:
    y = t - x
    ub = bisect_right(acc_b, y)
    lb = bisect_left(acc_b, y)
    answer += ub - lb

print(answer)
