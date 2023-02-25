# https://www.acmicpc.net/problem/3079

import sys

input = lambda: sys.stdin.readline().rstrip()

#############
def get_possible_count(time):
    total = 0
    for i in range(n):
        total += time // t[i]

    return total


n, m = map(int, input().split())
t = []
for _ in range(n):
    t.append(int(input()))

left = 1
right = int(1e20)
answer = 0
while left <= right:
    mid = (left + right) // 2

    count = get_possible_count(mid)

    if count >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
