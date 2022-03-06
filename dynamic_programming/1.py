n = int(input())
double = []
dp = [0] * n
for _ in range(n):
    double.append(float(input()))

dp[0] = double[0]
for i in range(1, n):
    if dp[i - 1] * double[i] > double[i]:
        dp[i] = dp[i - 1] * double[i]
    else:
        dp[i] = double[i]

print("{:.3f}".format(max(dp)))
