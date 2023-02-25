# https://www.acmicpc.net/problem/2512

n = int(input())
budget = list(map(int, input().split()))
m = int(input())


left = 0
right = max(budget)
while left <= right:
    mid = (left + right) // 2

    result = 0
    for b in budget:
        if b > mid:
            result += mid
        else:
            result += b

    if result <= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
