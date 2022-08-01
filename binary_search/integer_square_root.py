# https://www.acmicpc.net/problem/2417

n = int(input())

left = 0
right = 2 ** 33
answer = 0

while left <= right:
    mid = (left + right) // 2

    q2 = mid ** 2
    if q2 >= n:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
