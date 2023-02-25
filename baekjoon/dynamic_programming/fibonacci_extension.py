# https://www.acmicpc.net/problem/1788

n = int(input())
p = 1000000000


def fibo(n):
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % p
    return dp[i]


def fibo_extension(n):
    if n == 0:
        return 0
    if n == 1 or n == -1:
        return 1
    if n > 0:
        return fibo(n)
    else:
        sign = 1 if -n & 1 else -1
        return sign * fibo(-n)


res = fibo_extension(n)
if res == 0:
    print(0)
elif res < 0:
    print(-1)
else:
    print(1)
print(abs(res))
