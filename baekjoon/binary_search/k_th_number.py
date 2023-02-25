# https://www.acmicpc.net/problem/1300
# https://hongcoding.tistory.com/13

n = int(input())
k = int(input())

left = 1
right = n * n
answer = 0

# binary search
while left <= right:
    mid = (left + right) // 2

    temp = 0
    for i in range(1, n + 1):
        temp += min(mid // i, n)

    if temp < k:
        left = mid + 1
    else:
        right = mid - 1

print(left)
