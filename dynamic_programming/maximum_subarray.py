# https://www.acmicpc.net/problem/10211

for tc in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = array[0]
    for i in range(1, n):
        if dp[i - 1] + array[i] > array[i]:
            dp[i] = dp[i - 1] + array[i]
        else:
            dp[i] = array[i]

    print(max(dp))
