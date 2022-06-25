# https://www.acmicpc.net/problem/10025

n, k = map(int, input().split())
s = 1000000
x = [0] * (s + 1)
for _ in range(n):
    g, i = map(int, input().split())
    x[i] = g

if k * 2 + 1 >= s:
    print(sum(x))
    exit(0)

i = 0
j = 2 * k + 1
now = sum(x[i:j])
answer = now
while j <= s:
    now -= x[i]
    now += x[j]
    i += 1
    j += 1

    answer = max(answer, now)

print(answer)
