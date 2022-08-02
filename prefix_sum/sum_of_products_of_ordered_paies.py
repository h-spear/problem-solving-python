# https://www.acmicpc.net/problem/13900

n = int(input())
a = list(map(int, input().split()))
sa = [0] * (n + 1)
for i in range(1, n + 1):
    sa[i] = sa[i - 1] + a[i - 1]

answer = 0
for i in range(n):
    sum_others = sa[n] - sa[i + 1]
    answer += sum_others * a[i]

print(answer)
