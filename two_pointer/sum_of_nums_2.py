# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
a = list(map(int, input().split()))

i, j = 0, 1
cnt = 0
curr_sum = a[0]
while j <= n and i <= j:
    if curr_sum == m:
        cnt += 1
        curr_sum -= a[i]
        i += 1

    if j == n and curr_sum < m:
        break

    elif curr_sum < m:
        curr_sum += a[j]
        j += 1
    elif curr_sum > m:
        curr_sum -= a[i]
        i += 1

print(cnt)
