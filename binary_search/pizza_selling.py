# https://www.acmicpc.net/problem/2632

from bisect import bisect_left, bisect_right


t = int(input())
m, n = map(int, input().split())
a = [int(input()) for _ in range(m)]
b = [int(input()) for _ in range(n)]
la = len(a)
lb = len(b)
sa = [0, sum(a)]
sb = [0, sum(b)]
a.extend(a)
b.extend(b)


for i in range(1, la):
    for j in range(la):
        sa.append(sum(a[j : j + i]))

for i in range(1, lb):
    for j in range(lb):
        sb.append(sum(b[j : j + i]))

if len(sa) > len(sb):
    sa, sb = sb, sa

sb.sort()
answer = 0
for x in sa:
    y = t - x
    ub = bisect_right(sb, y)
    lb = bisect_left(sb, y)
    answer += ub - lb

print(answer)
