# https://www.acmicpc.net/problem/2851

n = 10
a = [int(input()) for _ in range(10)]
p_sum = [0] * (n + 1)
for i in range(1, n + 1):
    p_sum[i] = p_sum[i - 1] + a[i - 1]

answer = 0
t = 10000000
for x in p_sum:
    if abs(x - 100) <= t:
        if answer < x:
            answer = x
            t = abs(x - 100)

print(answer)
