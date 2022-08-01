# https://www.acmicpc.net/problem/16401


def func(length):
    cnt = 0
    for x in l:
        cnt += x // length

    return cnt


m, n = map(int, input().split())
l = list(map(int, input().split()))

answer = 0
l.sort(reverse=True)


left = 1
right = int(1e9)
while left <= right:
    mid = (left + right) // 2

    cnt = func(mid)
    if cnt < m:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(answer)
