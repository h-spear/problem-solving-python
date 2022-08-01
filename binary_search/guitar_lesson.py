# https://www.acmicpc.net/problem/2343


def is_seperated(length):
    cnt = 0
    temp = 0
    for x in l:
        if x > length:
            return False

        if temp + x > length:
            temp = x
            cnt += 1
        else:
            temp += x

    if temp:
        cnt += 1

    return cnt <= m


n, m = map(int, input().split())
l = list(map(int, input().split()))

answer = 0
left = 1
right = 1000000000

while left <= right:
    mid = (left + right) // 2

    if is_seperated(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
