# https://www.acmicpc.net/problem/1015

n = int(input())
a = list(map(int, input().split()))
sa = []
for i, x in enumerate(a):
    sa.append((x, i))
sa.sort()

p = [0] * n
for i, (_, x) in enumerate(sa):
    p[x] = i

print(*p)
