# https://www.acmicpc.net/problem/2473
# https://zu-techlog.tistory.com/25

import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
a.sort()
least = 4234567890
answer = []

for i in range(n - 2):
    left = i + 1
    right = n - 1
    while left < right:
        total = a[i] + a[left] + a[right]
        if abs(total) < least:
            least = abs(total)
            answer = [a[i], a[left], a[right]]

        if total < 0:
            left += 1
        elif total > 0:
            right -= 1
        else:
            break

print(*answer)
