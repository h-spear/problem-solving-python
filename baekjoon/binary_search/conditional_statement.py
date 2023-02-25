# https://www.acmicpc.net/problem/19637

import sys

input = lambda: sys.stdin.readline().rstrip()


def find_style(count):
    left = 0
    right = len(hash) - 1
    while left <= right:
        mid = (left + right) // 2

        if A[mid] == count:
            print(hash[A[mid]])
            return
        elif A[mid] < count:
            left = mid + 1
        else:
            right = mid - 1

    print(hash[A[right + 1]])
    return


n, m = map(int, input().split())
hash = {}
for _ in range(n):
    s, i = input().split()
    i = int(i)
    if i in hash:
        continue
    hash[i] = s

A = list(hash.keys())

for _ in range(m):
    find_style(int(input()))
