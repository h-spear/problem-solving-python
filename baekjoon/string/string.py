# https://www.acmicpc.net/problem/1120

a, b = input().split()
la = len(a)
lb = len(b)
dp = [0] * 51

for i in range(lb - la + 1):
    temp = 0
    for j in range(la):
        if a[j] == b[j + i]:
            temp += 1
    dp[i] = temp

print(la - max(dp))
