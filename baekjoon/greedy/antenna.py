# https://www.acmicpc.net/problem/18310

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

a.sort()
now = sum(a)
dict = defaultdict(int)
for x in a:
    dict[x] += 1

minima = 200000000000
acc = 0
answer = 0
for i in range(100000):
    acc += dict[i]
    now += acc
    now -= n - acc
    if now < minima:
        answer = i + 1
        minima = now

print(answer)
