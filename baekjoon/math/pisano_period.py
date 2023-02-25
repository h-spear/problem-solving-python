for tc in range(int(input())):
    n, m = map(int, input().split())

    dp = [0] * 1000000
    dp[1] = 1
    dp[2] = 2

    i = 3
    while 1:
        dp[i] = (dp[i - 1] + dp[i - 2]) % m
        if dp[i - 1] == 1 and dp[i] == 1:
            print(n, i - 1)
            break
        i += 1
