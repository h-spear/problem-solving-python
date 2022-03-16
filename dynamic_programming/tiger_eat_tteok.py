# https://www.acmicpc.net/problem/2502
# dp + bruteforce

d, k = map(int, input().split())
dp = [0] * 31


def simulate(a, b):
    dp[1] = a
    dp[2] = b
    for i in range(3, d + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[d]


def solve():
    a = 1
    b = 1
    while True:
        res = simulate(a, b)
        if res == k:
            return a, b
        if res > k:
            a += 1
            b = a
            continue
        b += 1


a, b = solve()
print(a)
print(b)
