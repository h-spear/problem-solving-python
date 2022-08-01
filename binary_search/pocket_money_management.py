# https://www.acmicpc.net/problem/6236


def get_minimum_withdrawal_count(k):
    cnt = 0
    temp = 0
    for price in prices:
        if price > k:
            return 1111111111

        if temp + price <= k:
            temp += price
            continue

        temp = price
        cnt += 1

    if temp:
        cnt += 1

    return cnt


n, m = map(int, input().split())
prices = []
for _ in range(n):
    prices.append(int(input()))

left = 1
right = int(1e11)
answer = 0
while left <= right:
    mid = (left + right) // 2

    cnt = get_minimum_withdrawal_count(mid)
    if cnt <= m:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
