# https://www.acmicpc.net/problem/14607

# n = int(input())
# print(n * (n - 1) // 2)


def fn(c):
    if c <= 1:
        return
    k = c // 2
    n = c - k
    if k not in dp:
        fn(k)
    if n not in dp:
        fn(n)

    dp[c] = n * k + dp[n] + dp[k]


dp = {1: 0}
n = int(input())
fn(n)
print(dp[n])
