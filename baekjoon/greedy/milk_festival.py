# https://www.acmicpc.net/problem/14720

n = int(input())
m = list(map(int, input().split()))
answer = 0
t = 0

for milk in m:
    if milk == t:
        answer += 1
        t = (t + 1) % 3

print(answer)
