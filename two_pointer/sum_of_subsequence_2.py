# https://www.acmicpc.net/problem/1208
# meet in the middle

from itertools import combinations
from bisect import bisect_right, bisect_left

n, s = map(int, input().split())
a = list(map(int, input().split()))
b = a[(n // 2) :]
a = a[: (n // 2)]
sa = []
sb = []

answer = 0
for i in range(1, len(a) + 1):
    for candidate in combinations(a, i):
        total = sum(candidate)
        sa.append(total)

        if total == s:
            answer += 1

for i in range(1, len(b) + 1):
    for candidate in combinations(b, i):
        total = sum(candidate)
        sb.append(total)

        if total == s:
            answer += 1

sb.sort()

for num in sa:
    target = s - num
    count = bisect_right(sb, target) - bisect_left(sb, target)
    answer += count


print(answer)
